# serializers.py

from rest_framework import serializers
from .models import Product, Seller, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'description', 'image']


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'logo', 'rating', 'warranty_offer']


class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()
    reviews = ReviewSerializer(many=True, required=False)  # Make reviews optional

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'original_price', 'offer_price', 'images', 'seller', 'reviews']

    def create(self, validated_data):
        # Pop the seller and review data separately
        seller_data = validated_data.pop('seller')
        reviews_data = validated_data.pop('reviews', [])  # Default to an empty list if 'reviews' is missing

        # Handle the seller: either get or create a seller
        seller, _ = Seller.objects.get_or_create(name=seller_data['name'], defaults=seller_data)

        # Create the product with the remaining validated data and the seller instance
        product = Product.objects.create(seller=seller, **validated_data)

        # Create reviews if any exist
        for review_data in reviews_data:
            Review.objects.create(product=product, **review_data)

        return product
