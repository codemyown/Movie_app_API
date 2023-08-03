from django.shortcuts import render
from django.http import HttpResponse
from .models.contact import Contact
from .models.contact import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.gallary import Gallary
from .models.gallary import GallarySerializer
from .models.movie import Movie
from .models.movie import MovieSerializer
from .models.about import About

# Create your views here.

def index(request):
	gallarys = Gallary.objects.all()
	movies = Movie.objects.all()
	about = About.objects.all()
	data = {
	'gallary':gallarys,
	'movie':movies,
	'about':about
	}
	return render(request,'index.html',data)



def contact(request):
	if request.method == "POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		phone = request.POST['phone']
		movie = request.POST['movie']
		message = request.POST['message']
		my_contact = Contact(First_Name = firstname,Last_Name = lastname,Phone = phone,Movie_Name = movie,Message = message)
		my_contact.save()


	return render(request,'contact.html')


@api_view(['GET'])
def api_contact(request):
	contact = Contact.objects.all()
	contact_serializer = ContactSerializer(contact,many = True)
	my_data = contact_serializer.data
	return Response({"message":my_data})


@api_view(['GET','POST'])
def gallaryAPI(request):
	if request.method == 'GET':
		gallary = Gallary.objects.all()
		gallarySerializer = GallarySerializer(gallary,many = True)
		return Response(gallarySerializer.data)

	elif request.method == 'POST':
		gallarys = GallarySerializer(data = request.data)
		if gallarys.is_valid():
			gallarys.save()
			return Response(gallarys.data)
		else:
			return Response(gallarys.errors)
			

@api_view(['GET','POST'])
def movieAPI(request):
	if request.method == 'GET':
		movies = Movie.objects.all()
		serialize_movie = MovieSerializer(movies,many= True)
		return Response(serialize_movie.data)

	elif request.method == 'POST':
		movies_s = MovieSerializer(data = request.data)
		if movies_s.is_valid():
			movies_s.save()
			return Response(movies_s.data)
		else:
			return Response(movies_s.errors)

