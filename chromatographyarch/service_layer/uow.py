from __future__ import annotations
import abc
from django.db import transaction
from chromatographyarch.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    analyticalmethods: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class DjangoUnitofWork(AbstractUnitOfWork):
    def __enter__(self):
        self.analyticalmethods = repository.DjangoRepository()

        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        with transaction.atomic():
            for am in self.analyticalmethods.analyticalmethods_set:
                print(f"committing analyticalmethod: {str(am)}")
                self.analyticalmethods.update(am)

    def rollback(self):
        pass


class DjangoApiUnitofWork(AbstractUnitOfWork):
    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def commit(self):
        super().commit()
        pass

    def rollback(self):
        pass
