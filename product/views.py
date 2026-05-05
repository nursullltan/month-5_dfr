from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import ProductListSerializer, ReviewListSerializer, CategoryListSerializer, CategoryDetailSerializer,ReviewDetailSerializer, ProductDetailSerializer, ProductReviewsSerializer


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(category, many=False).data
    return Response(data=data)


@api_view(['GET'])
def category_list_api_view(request):
    categorys = Category.objects.all()
    data = CategoryListSerializer(categorys, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product, many=False).data
    return Response(data=data)

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductListSerializer(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_reviews_list_api_view(request):
    products = Product.objects.all()
    data = ProductReviewsSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view (request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review, many=False).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)



        


    


    

# Create your views here.
