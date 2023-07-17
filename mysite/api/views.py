from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# Create your views here.
def api_home(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    # print(data)
    # print("GET :", request.GET)
    # print("POST :", request.POST)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)


@api_view(['GET', "POST"])
def product(request):
    if request.method == 'GET':
        data = {}
        item = Product.objects.all().first()
        # data['id'] = item.id  #1
        # data['title'] = item.title
        # data['des'] = item.des
        # data['price'] = item.price
        # data = model_to_dict(item, fields=['id', 'title', 'price', 'sale_price'])  # 2
        data = ProductSerializer(item, many=False).data
        return Response(data)
    elif request.method == 'POST':
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # product_item = serializer.save()  # return a Product object
            print(serializer.data)
            data = serializer.data
            return Response(data)
