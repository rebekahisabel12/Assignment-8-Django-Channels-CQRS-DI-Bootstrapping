from typing import Set
import abc
from chromatographyarch.domain.model import DomainAnalyticalMethod
from an_organ.models import AnalyticalMethod


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.analyticalmethods_set = set()

    def add(self, analyticalmethod: DomainAnalyticalMethod):
        self.analyticalmethods_set.add(analyticalmethod)

    def get(self, method_name) -> DomainAnalyticalMethod:
        analyticalmethod = self._get(method_name)
        if analyticalmethod:
            self.analyticalmethods_set.add(analyticalmethod)
        return analyticalmethod

    @abc.abstractmethod
    def _get(self, method_name):
        raise NotImplementedError


class DjangoRepository(AbstractRepository):

    def add(self, analyticalmethod):
        super().add(analyticalmethod)
        self.update(analyticalmethod)

    def update(self, analyticalmethod):
        AnalyticalMethod.update_from_domain(analyticalmethod)

    def _get(self, method_name):
        return AnalyticalMethod.objects.filter(method_name=method_name).first().to_domain()

    def list(self):
        return [analyticalmethod.to_domain() for analyticalmethod in AnalyticalMethod.objects.all()]


class DjangoAPIRepository(AbstractRepository):

    def add(self, analyticalmethod):
        pass

    def update(self, analyticalmethod):
        pass

    def _get(self, method_name):
        pass

    def list(self):
        pass
