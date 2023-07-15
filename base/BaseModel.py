from django.db import models
import uuid

class Base_Model(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta():
        abstract=True

