# models.py
from django.db import models


class Admin(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=32,null=False)
    password = models.CharField(max_length=32,null=False)
    # update_time = models.PositiveIntegerField(default=0,null=False)
    update_time = models.PositiveIntegerField(default=0,null=False)

    class Meta:
        db_table = 'test'