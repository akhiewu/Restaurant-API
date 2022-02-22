from rest_framework import serializers
from myapp.models import Restaurant, Catagory, Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__' 
        #depth = 1 

class RestaurantSerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = Restaurant
        fields = '__all__'
        #depth = 1
        
    def get_food(self, obj):
        serializer = FoodSerializer(obj.foods, many=True) 
        return serializer.data     
        
class CategorySerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = Catagory
        fields = '__all__'
       # depth = 1 
         
    def get_food(self, obj):
        serializer = FoodSerializer(obj.foods, many=True) 
        return serializer.data        
                      
           
 
        
                   