from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime
from django.contrib.auth.models import User
from unittest.mock import Mock

from an_organ.models import AnalyticalMethod, Instrument
from chromatographyarch.domain.model import DomainAnalyticalMethod, DomainInstrument
from chromatographyarch.adapters import repository
from chromatographyarch.service_layer.uow import DjangoUnitofWork
from chromatographyarch.service_layer.commands import AddAnalyticalMethodCommand, AddInstrumentCommand


class TestCommands(TestCase):
    def setUp(self):
        rightnow = localtime().date()

        # instrument = Instrument.objects.create(
        #     instrument_id="432",
        #     manufacturer="Odessa Analyzer",
        #     sample_type="Solid"
        # )
        self.user = User.objects.create(username="username")

    def test_add_instrument_command(self):
        domain_instrument = DomainInstrument(
            instrument_id="432",
            manufacturer="Odessa Analyzer",
            sample_type="Solid"
        )
        owner = Mock(spec=User)

        add_instrument_command = AddInstrumentCommand()
        add_instrument_command.execute(domain_instrument)

        self.assertEqual(Instrument.objects.count(), 1)
        instrument = Instrument.objects.first()
        self.assertEqual(instrument.instrument_id, "432")
        self.assertEqual(instrument.manufacturer, "Odessa Analyzer")
        self.assertEqual(instrument.sample_type, "Solid")

        # def test_add_analytical_method_command(self):

        #     owner = Mock(spec=User)

        #     command = AddAnalyticalMethodCommand()
        #     command.execute(self.domain_analyticalmethod_1, owner)

        #     analytical_method = AnalyticalMethod.objects.get(
        #         method_name="Test Method 1")
        #     self.assertEqual(analytical_method.method_name, "Test Method 1")
