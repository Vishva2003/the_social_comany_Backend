from rest_framework import viewsets
from .models import Product, Review, Seller
from .serializers import ProductSerializer, ReviewSerializer, SellerSerializer
from rest_framework.parsers import MultiPartParser, FormParser



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer