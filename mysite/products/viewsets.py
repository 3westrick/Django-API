from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializerV2


class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> show instance
    post -> create
    put -> update full columns
    patch -> partial update
    delete -> delete obj
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV2
    lookup_field = 'pk'


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    get -> list -> queryset
    get -> retrieve -> show instance
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV2
    lookup_field = 'pk'
