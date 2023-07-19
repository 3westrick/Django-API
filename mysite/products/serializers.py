from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, validate_no_hello_allowed, unique_product_title
from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(validators=[validate_no_hello_allowed, unique_product_title])

    # email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'des',
            'price',
            'sale_price',
            'discount',
            'url',
            'edit_url',
            'owner',
            # 'email',
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    def create(self, validated_data):
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        # print(email, obj) # send email
        return obj

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)

    def get_url(self, obj):
        # return f"/api/products/{obj.id}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={'pk': obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        try:
            return obj.get_discount()
        except:
            return None


class ProductSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'des',
        ]
