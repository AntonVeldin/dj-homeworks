from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['quantity', 'price', 'stock_id', 'product']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for pos in positions:
            StockProduct(
                stock=stock,
                product=pos['product'],
                quantity=pos['quantity'],
                price=pos['price']
                ).save()
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for pos in positions:
            obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=pos['product'],
                defaults=pos
            )
        return stock
