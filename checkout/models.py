from django.db import models


# Create your models here.


class CheckoutLine(models.Model):
    variant = models.ForeignKey(null=False, blank=False, max_length=255)
    quantity = models.IntegerField(null=False, blank=False)
    checkout = models.ForeignKey(null=False, blank=False, max_length=255)


class Checkout(models.Model):
    user = models.ForeignKey()
    lines = models.ManyToOne(null=False, blank=False)
    user_email = models.EmailField(null=False, blank=False)