from graphene_django import DjangoObjectType
import graphene
from ...checkout.models import Checkout, CheckoutLine
from django.db.models import Sum


class CheckoutType(DjangoObjectType):
    class Meta:
        model = Checkout
        fields = "__all__"

    def resolve_total_price(self, _info):
        checkout = self.lines.all().aggregate(sum_checkout_price=Sum('variant__price'))
        sum_checkout_price = checkout['sum_checkout_price']
        if not sum_checkout_price:
            return self.lines

class CheckoutLineType(DjangoObjectType):
    class Meta:
        model = CheckoutLine
        fields = "__all__"

    def resolve_total_price(self, _info):
        checkout_line_price = self.variant.price*self.quantity
        if not checkout_line_price:
            return self.variants

        return checkout_line_price