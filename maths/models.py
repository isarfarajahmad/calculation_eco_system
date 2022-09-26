from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Submission(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    metric = models.CharField(max_length=100, null=True)
    subject1 = models.IntegerField(null=True)
    subject2 = models.IntegerField(null=True)
    value = models.FloatField(max_length=1000, null=True)
    file = models.FileField(upload_to='upload/files', null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.metric
