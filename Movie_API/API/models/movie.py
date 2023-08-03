from django.db import models
from rest_framework import serializers


class Movie(models.Model):
	image = models.ImageField(upload_to = 'upload/images')
	name = models.CharField(max_length = 30)
	story = models.CharField(max_length = 100)
	desc = models.CharField(max_length = 200)



	def __str__(self):
		return self.name


class MovieSerializer(serializers.Serializer):
	image = serializers.ImageField()
	name = serializers.CharField(max_length = 30)
	story = serializers.CharField(max_length = 100)
	desc = serializers.CharField(max_length = 200)

	def create(self,validated_data):
		return Movie.objects.create(**validated_data)
		
		