from .repositories import AnalyticalMethodRepository


class AnalyticalMethodService:
    def __init__(self):
        self.repository = AnalyticalMethodRepository()

    def create_method(self, owner, method_name, method_description, instrument, cost_per_sample):
        return self.repository.create_method(owner, method_name, method_description, instrument, cost_per_sample)

    def get_method_by_id(self, method_id):
        return self.repository.get_method_by_id(method_id)

    def update_method(self, method_id, **kwargs):
        return self.repository.update_method(method_id, **kwargs)

    def delete_method(self, method_id):
        return self.repository.delete_method(method_id)
