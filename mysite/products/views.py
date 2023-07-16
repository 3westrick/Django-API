from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        des = serializer.validated_data.get('des')
        if des is None:
            des = title
        serializer.save(des=des)


@api_view(['GET', 'POST'])
def product_list_create(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)
    if request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # product_item = serializer.save()  # return a Product object
            title = serializer.validated_data.get('title')
            des = serializer.validated_data.get('des')
            if des is None:
                des = title
            serializer.save(des=des)
            data = serializer.data
            return Response(data)
