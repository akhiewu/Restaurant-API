from django.shortcuts import render
from myapp.models import Restaurant, Catagory, Food
from myapp.serializers import RestaurantSerializer, CategorySerializer, FoodSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status






@api_view(['GET'])       # Catagory id with code
def get_catagory1(request,id):
    catagory_objs = Catagory.objects.filter(id=id).first()
    serializer = CategorySerializer(catagory_objs)
    return Response({'status':200, 'category': serializer.data})


@api_view(['GET'])       # Restaurant id with code
def get_restaurant1(request,id):
    restaurant_objs = Restaurant.objects.filter(id=id).first()
    serializer = RestaurantSerializer(restaurant_objs)
    return Response({'status':200, 'restaurant': serializer.data})



#--------------------------------------Restaurant---------------------------------------------


class RestaurantList(APIView):
    
    def get(self, request, format=None):
        restaurant_var = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant_var, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class RestaurantDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant_varr = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant_varr)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        restaurant_varr = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant_varr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        restaurant_varr = self.get_object(pk)
        restaurant_varr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#---------------------------------------------------------------------------------------------------------------------
#                                               Catagory
#----------------------------------------------------------------------------------------------------------------


class CatagoryList(APIView):
    
    def get(self, request, format=None):
        catagory_var = Catagory.objects.all()
        serializer = CategorySerializer(catagory_var, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class CategoryDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        catagory_varr = self.get_object(pk)
        serializer = CategorySerializer(catagory_varr)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        catagory_varr = self.get_object(pk)
        serializer = CategorySerializer(catagory_varr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        catagory_varr = self.get_object(pk)
        catagory_varr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#-----------------------------------------------------------------------------------------------
#                                           Food
#--------------------------------------------------------------------------------------------------------


class FoodList(APIView):
    
    def get(self, request, format=None):
        food_var = Food.objects.all()
        serializer = FoodSerializer(food_var, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class FoodDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        food_varr = self.get_object(pk)
        serializer = FoodSerializer(food_varr)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        food_varr = self.get_object(pk)
        serializer = FoodSerializer(food_varr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        food_varr = self.get_object(pk)
        food_varr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





#--------------------------------------------------------------------------------------





