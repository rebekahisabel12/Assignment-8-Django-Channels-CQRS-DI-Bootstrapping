from datetime import date
from typing import List, Optional, Set


class DomainInstrument:
    def __init__(self, instrument_id, manufacturer, sample_type):
        self.instrument_id = instrument_id
        self.manufacturer = manufacturer
        self.sample_type = sample_type

    def __str__(self):
        return f"{self.manufacturer} - {self.sample_type}"


class DomainAnalyticalMethod:

    def __init__(self, method_name, method_description, instrument, cost_per_sample, owner=None):
        self.method_name = method_name
        self.method_description = method_description
        self.instrument = instrument
        self.cost_per_sample = cost_per_sample
        self.owner = owner

    def __str__(self):
        return f"self.method_name"
