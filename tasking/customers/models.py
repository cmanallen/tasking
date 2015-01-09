from django.db import models
from tenant_schemas.models import TenantMixin

# Create your models here.
class Client(TenantMixin):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=255, blank=True)
  trial = models.BooleanField()
  expiration = models.DateField(blank=True)
