import graphene
from .types import CheckoutType, CheckoutLineType
from ...checkout.models import Checkout, CheckoutLine


class CheckoutCreateInput(graphene.InputObjectType):
    user = graphene.ID()
    user_email = graphene.String(required=True)


class CheckoutLineCreateInput(graphene.InputObjectType):
    quantity = graphene.Int(required=True)


class CheckoutCreate(graphene.Mutation):
    checkout = graphene.Field(CheckoutType)

    class Arguments:
        input = CheckoutCreateInput(required=True)
        lines_id = graphene.ID(required=True)

    @classmethod
    def clean_input(cls, input):
        return input

    @classmethod
    def mutate(cls, root, _info, input, lines_id):
        cleaned_input = cls.clean_input(input)

        checkout = Checkout.objects.create(lines_id=lines_id, **cleaned_input)

        return CheckoutCreate(checkout=checkout)


class CheckoutLineCreate(graphene.Mutation):
    checkout_line = graphene.Field(CheckoutLineType)

    class Arguments:
        input = CheckoutLineCreateInput(required=True)
        variant_id = graphene.ID(required=True)
        checkout_id = graphene.ID(required=True)

    @classmethod
    def clean_input(cls, input):
        return input

    @classmethod
    def mutate(cls, root, _info, input, variant_id, checkout_id):
        cleaned_input = cls.clean_input(input)
        checkout_line = CheckoutLine.obejcts.create(variant_id=variant_id, checkout_id=checkout_id, **cleaned_input)

        return CheckoutLineCreate(checkout_line=checkout_line)