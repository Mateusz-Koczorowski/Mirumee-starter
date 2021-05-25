import graphene
from .types import CheckoutLineType, CheckoutType
from ...checkout.models import Checkout, CheckoutLine
from .mutations import CheckoutCreate, CheckoutLineCreate


class CheckoutQueries(graphene.ObjectType):
    checkout = graphene.Field(CheckoutType, id=graphene.Argument(graphene.ID, description="ID of checkout"))
    checkout_line = graphene.Field(CheckoutLineType, id=graphene.Argument(graphene.ID, description="ID of checkout line"))

    def resolve_checkout(self, _info, id):
        checkout = Checkout.objects.filter(id=id).first()
        return checkout

    def resolve_checkouts(self, _info):
        checkouts = Checkout.objects.all()
        return checkouts

    def resolve_checkout_line(self, info, id):
        return CheckoutLine.object.filter(id=id).first()


class CheckoutMutations(graphene.ObjectType):
    checkout_create = CheckoutCreate.Field()
    checkout_line_create = CheckoutLineCreate.Field()