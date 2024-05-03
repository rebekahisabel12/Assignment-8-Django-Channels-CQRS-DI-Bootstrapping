import asyncio
import datetime
import json

from channels.consumer import AsyncConsumer, SyncConsumer
from channels.generic.http import AsyncHttpConsumer

from an_organ.models import AnalyticalMethod, Instrument


class SimpleInstrumentConsumer(AsyncConsumer):
    async def print_instrument(self, message):
        print(f"WORKER: Instrument: {message['data']}")


class InstrumentConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        instruments = Instrument.objects.all()
        data = json.dumps(
            [{"instrument_id": instrument.instrument_id,
                "manufacturer": instrument.manufacturer} for instrument in instruments]
        )
        await self.send_response(
            200, data, headers=[(b"Content-Type", b"application/json")]
        )

    async def handle(self, body):
        await self.send_headers(
            headers=[
                (b"Cache-control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
            ]
        )
        while True:
            payload = "data: %s\n\n" % datetime.now().isoformat()
            await self.send_body(payload.encode("utf-8"), more_body=True)
            await asyncio.sleep(1)

    async def send_instrument(self, instrument):
        data = json.dumps({"instrument_id": instrument.instrument_id,
                          "manufacturer": instrument.manufacturer})
        await self.channel_layer.send(
            "instruments-add", {"type": "send.instrument", "data": data}
        )
