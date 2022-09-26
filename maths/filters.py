import django_filters
from .models import *

class SubmissionFilter(django_filters.FilterSet):
    class Meta:
        model = Submission
        fields = ['user','metric']