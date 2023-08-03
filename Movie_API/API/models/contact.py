from django.db import models
from rest_framework import serializers 



class Contact(models.Model):
	First_Name = models.CharField(max_length = 30)
	Last_Name = models.CharField(max_length  = 40)
	Phone = models.IntegerField(default = 0)
	Movie_Name = models.CharField(max_length = 50)
	Message = models.CharField(max_length = 200	)


	def __str__(self):
		return self.Movie_Name


class ContactSerializer(serializers.Serializer):
	First_Name = serializers.CharField(max_length = 30)
	Last_Name = serializers.CharField(max_length  = 40)
	Phone = serializers.IntegerField(default = 0)
	Movie_Name = serializers.CharField(max_length = 50)
	Message = serializers.CharField(max_length = 200)


