from .models import AnalyticalMethod


class AnalyticalMethodRepository:
    def create_method(self, owner, method_name, method_description, instrument=None, cost_per_sample=None):
        if not method_name or not cost_per_sample:
            raise ValueError("Method name and cost per sample are required.")
        return AnalyticalMethod.objects.create(
            owner=owner,
            method_name=method_name,
            method_description=method_description,
            instrument=instrument,
            cost_per_sample=cost_per_sample

        )

    def get_method_by_id(self, method_id):
        return AnalyticalMethod.objects.get(pk=method_id)

    def update_method(self, method_id, **kwargs):
        method = AnalyticalMethod.objects.get(pk=method_id)
        for key, value in kwargs.items():
            setattr(method, key, value)
        method.save()

    def delete_method(self, method_id):
        AnalyticalMethod.objects.filter(pk=method_id).delete()
