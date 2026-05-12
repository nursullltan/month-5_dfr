from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Review, Category
from .serializers import ProductListSerializer, ReviewListSerializer, CategoryListSerializer, CategoryDetailSerializer,ReviewDetailSerializer, ProductDetailSerializer, ProductReviewsSerializer


@api_view(['GET', 'PUT', 'DELET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        data = CategoryDetailSerializer(category, many=False).data
        return Response(data=data)  
    elif request.method == 'DELET':
        category.delet()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        category.name = request.data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                    data=ReviewListSerializer(category))


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        data = CategoryListSerializer(categorys, many=True).data
        return Response(data=data)
    
    elif request.method == 'POST':
        name = request.data.get('name')

    category = Category.objects.create(
        name=name
    )
    category.save()
    return Response(status=status.HTTP_201_CREATED)
    



@api_view(['GET', 'PUT', 'DELET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'DELET':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
        product.save()
        return Response(status=status.HTTP_201_CREATED,
                    data=ReviewListSerializer(product))

@api_view(['GET'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductListSerializer(products, many=True).data
        return Response(data=data)
    
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

    product = Product.objects.create(
        title=title,
        description=description,
        price=price,
        category_id=category_id
    )
    product.save()
    return Response(
        status=status.HTTP_201_CREATED,
        data=ProductListSerializer.data)
    

@api_view(['GET'])
def product_reviews_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductReviewsSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    

        


@api_view(['GET', 'PUT', 'DELET'])
def review_detail_api_view (request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewDetailSerializer(review, many=False).data
        return Response(data=data)
    elif request.method == 'DELET':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        review.text = request.data.get('text')
        review.product_id = request.datd.get('product_id')
        review.stars = request.data.get('stars')
        return Response(status=status.HTTP_201_CREATED,
                    data=ReviewListSerializer(review))

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
      
    elif request.method == "POST":
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')

    review = Review.objects.create(
        text=text,
        product_id=product_id,
        stars=stars
    )
    review.save()
    return Response(status=status.HTTP_201_CREATED,
                    data=ReviewListSerializer(review))


        


    


    

# Create your views here.
