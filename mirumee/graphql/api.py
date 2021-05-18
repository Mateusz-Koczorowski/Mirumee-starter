import graphene
from ..graphql.product.schema import ProductQueries, ProductMutations, ProductVariantMutations


class Query(ProductQueries):
    pass


schema = graphene.Schema(query=Query)


class Mutations(ProductMutations, ProductVariantMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)