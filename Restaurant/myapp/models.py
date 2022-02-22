import email
from django.db import models


class Restaurant(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank = True)
    def __str__(self):
        return self.name  
      
      
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    image = models.ImageField(blank = True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name = 'foods')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name = 'foods' )
    
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'catagory':
                return(field.name, self.catagory.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]
        
    def get_fields(self):
        def get_dynamic_fields(field):
            if field.name == 'restaurant':
                return(field.name, self.restaurant.name, field.get_internal_type())
            else:
                return(field.name, self.value_from_object(self), field.get_internal_type())
            return[get_dynamic_fields(field) for field in self.__class__._meta.fields]    
    
          