import sys
from abc import ABC, abstractmethod
from datetime import datetime
import pytz

import requests
from django.db import transaction
from django.contrib.auth.models import User

from an_organ.models import AnalyticalMethod, Instrument
from chromatographyarch.domain.model import DomainAnalyticalMethod, DomainInstrument


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(
            "A command must implement the execute method")


class AddInstrumentCommand(Command):
    def execute(self, data: DomainInstrument):
        instrument = Instrument.objects.create(
            instrument_id=data.instrument_id,
            manufacturer=data.manufacturer,
            sample_type=data.sample_type,
        )
        with transaction.atomic():
            instrument.save()


# class ListInstrumentsCommand(Command):
#     def __init__(self, order_by="instrument_id"):
#         self.order_by = order_by

#     def execute(self, data=None):
#         return Instrument.objects.all().order_by(self.order_by)


# class DeleteInstrumentCommand(Command):
#     def execute(self, data):
#         instrument = Instrument.objects.get(instrument_id=data.instrument_id)
#         with transaction.atomic():
#             instrument.delete()


# class EditInstrumentCommand(Command):
#     def execute(self, data):
#         try:
#             instrument = Instrument.objects.get(
#                 instrument_id=data.instrument_id)
#         except Instrument.DoesNotExist:
#             instrument = Instrument(instrument_id=data.instrument_id)

#         instrument.manufacturer = data.manufacturer
#         instrument.sample_type = data.sample_type

#         instrument.save()


class AddAnalyticalMethodCommand(Command):
    def execute(self, data: DomainAnalyticalMethod, owner: User, timestamp=None):
        analyticalmethod = AnalyticalMethod(
            method_name=data.method_name, method_description=data.method_description, instrument=data.instrument, cost_per_sample=data.cost_per_sample, owner=owner, timestamp=timestamp)

        with transaction.atomic():
            analyticalmethod.save()


# class ListAnalyticalMethodsCommand(Command):

#     def __init__(self, order_by="date_added"):
#         self.order_by = order_by

#     def execute(self, data=None):
#         return AnalyticalMethod.objects.all().order_by(self.order_by)


# class DeleteAnalyticalMethodCommand(Command):

#     def execute(self, data: DomainAnalyticalMethod):
#         analyticalmethod = AnalyticalMethod.objects.get(url=data.url)
#         with transaction.atomic():
#             analyticalmethod.delete()


# class EditAnalyticalMethodCommand(Command):

#     def execute(self, data: DomainAnalyticalMethod, owner: User):
#         try:
#             analyticalmethod = AnalyticalMethod.objects.get(
#                 method_name=data.method_name)
#         except AnalyticalMethod.DoesNotExist:
#             analyticalmethod = AnalyticalMethod(method_name=data.method_name)

#         analyticalmethod.method_description = data.method_description
#         analyticalmethod.instrument = data.instrument
#         analyticalmethod.cost_per_sample = data.cost_per_sample
#         analyticalmethod.owner = owner

#         analyticalmethod.save()
