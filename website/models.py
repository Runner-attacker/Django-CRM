from django.db import models
from dateutil.relativedelta import relativedelta
import datetime


class Ottplatform(models.Model):
    Platform = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(null=True, blank=True, max_length=100)
    profile = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.Platform


class Record(models.Model):
    created_at = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    platform = models.ForeignKey(Ottplatform, on_delete=models.DO_NOTHING)
    useful_month = models.IntegerField()
    expiry_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=10, default="Active"
    )  # Status field with default value 'Active'

    def save(self, *args, **kwargs):
        if self.useful_month:
            # Calculate expiry_date
            self.expiry_date = self.created_at + relativedelta(months=self.useful_month)

        # Update status based on expiry_date
        if self.expiry_date and self.expiry_date < datetime.date.today():
            self.status = "Expired"
        else:
            self.status = "Active"

        super(Record, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
