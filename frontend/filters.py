import django_filters

from meds.models import Med

class MedFilter(django_filters.FilterSet):
    class Meta:
        model = Med
        fields = ['med_name',]