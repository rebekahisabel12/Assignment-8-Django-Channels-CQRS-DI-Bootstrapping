import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SimpleInstrumentConsumer
from .models import AnalyticalMethod, Instrument

channel_layer = get_channel_layer()


def log_instrument_to_csv(sender, instance, **kwargs):
    print("Instrument signal: CSV")

    file = Path(__file__).parent.parent / "chromatographyarch" / \
        "domain" / "instrument_log.csv"
    print(f"Writing to {file}")

    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        logwriter.writerow(
            [
                instance.instrument_id,
                instance.manufacturer,
                instance.sample_type,
            ]
        )


def send_instrument_to_channel(sender, instance, **kwargs):
    print("Instrument signal: Channel")
    print(f"Sending instrument to channel: {instance}")

    async_to_sync(channel_layer.send)(
        "instruments-add", {"type": "print.instrument",
                            "data": instance.manufacturer}
    )


post_save.connect(log_instrument_to_csv, sender=Instrument)
post_save.connect(send_instrument_to_channel, sender=Instrument)


# def log_analyticalmethod_to_csv(sender, instance, **kwargs):
#     print("I am a signal! I was called because an Analytical method was saved!")

#     file = Path(__file__).parent.parent / "chromatographyarch" / \
#         "domain" / "created_log.csv"
#     print(f"Writing to {file}")

#     with open(file, "a+", newline="") as csvfile:
#         logfile = File(csvfile)
#         logwriter = csv.writer(
#             logfile,
#             delimiter=",",
#         )
#         logwriter.writerow(
#             [
#                 instance.method_name,
#                 instance.method_description,
#                 instance.cost_per_sample,
#                 instance.instrument,
#                 instance.owner,
#             ]
#         )


# def send_analytical_method_to_channel(sender, instance, **kwargs):
#     print("Analytical Method signal: Channel")
#     print(f"Sending bookmark to channe: {instance}")

#     async_to_sync(channel_layer.send)(
#         "analyticalmethods-add", {"type": "print.analyticalmethod",
#                                   "data": instance.url}
#     )


# post_save.connect(log_analyticalmethod_to_csv, sender=AnalyticalMethod)
# post_save.connect(send_analyticalmethod_to_channel, sender=AnalyticalMethod)
