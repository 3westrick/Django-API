from rest_framework import serializers


class ProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='product-detail',
    #     lookup_field='pk',
    #     read_only=True,
    # )


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        request = self.context.get('request')

        print("---------------------")
        print(request.auth)
        print(request.authenticators)
        print(request.query_params)
        print(request.user)
        print("---------------------")
        user = obj
        user_products = user.product_set.all()[:5]
        return ProductInlineSerializer(user_products, many=True).data
