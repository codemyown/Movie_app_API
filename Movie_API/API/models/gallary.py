from django.db import models
from rest_framework import serializers


class Gallary(models.Model):
	image = models.ImageField(upload_to = 'upload/images')
	title = models.CharField(max_length = 30)
	desc = models.CharField(max_length = 100)



	def __str__(self):
		return self.title

class GallarySerializer(serializers.Serializer):
	image = serializers.ImageField()
	title = serializers.CharField(max_length = 30)
	desc = serializers.CharField(max_length = 100)


	def create(self,validated_data):
		return Gallary.objects.create(**validated_data)
		
		