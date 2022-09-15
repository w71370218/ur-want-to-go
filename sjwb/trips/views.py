from django.shortcuts import render, redirect, get_object_or_404
#建立首頁
from trips.models import Post, Like, Tag, Comment
from .forms import PostForm, post_comment_form
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
#folium
import folium
from folium.plugins import MarkerCluster
#imgur
import pyimgur
CLIENT_ID = settings.CLIENT_ID
im = pyimgur.Imgur(CLIENT_ID)

import requests
import geopandas

# webparser
"""
map_url =  'https://data.moi.gov.tw/MoiOD'
href="/System/DownloadFile.aspx?DATA=72874C55-884D-4CEA-B7D6-F60B0BE85AB0"
response = requests.get(map_url + href)
with open('County.zip', 'wb') as file:
	file.write(response.content)
	file.close()
"""
import os
dir = os.getcwd()
counties_gdf = geopandas.read_file(dir+ '\\media\\'+'County.zip')

def home(request):
	posts = Post.objects.all()
	
	#map
	m = folium.Map(location=[23.97565,120.9738819], zoom_start=8, height="100%", position="initial")

	# County layer
	folium.GeoJson(data=counties_gdf["geometry"], name="縣市分區").add_to(m)

	marker_cluster = MarkerCluster(control=False).add_to(m)
	style_attraction = {'color': 'red'}
	style_restaurant = {'color': 'green', 'icon':'utensils', 'prefix':'fa'}
	style_accomodation = {'color': 'blue', 'icon':'bed', 'prefix':'fa'}
	
	mCluster = MarkerCluster(name="景點數量").add_to(m)

	for post in posts:
		#popup = '<h1>' + post.title + '</h1>'
		#stars
		stars = '<span style="' + 'color:#ffbb04">'
		for i in range(1,6):
			if i <= post.stars:
				stars = stars + '★'
			else:
				stars = stars + '☆'
		stars = stars + '</span>'

		popup = '<div class="popup"><a href="/post/'+ str(post.pk) +'" target="_parent" style="text-decoration: none; color:#000"><h1>' + post.title + '</h1>'\
			+ '<h4>'+ post.location +'</h4>'\
			+ '<h4>想去指數: '+ stars +'</h4>'
		if post.imgur_url:
			popup  = popup + '<img src="'+ post.imgur_url + '" style="width:350px;"></a>'
		else:
			popup  = popup + '<img src="'+ "/media/no_image.jpg" + '" style="width:350px;"></a></div>'
		match post.category:
			case 1:
				color = 'red'
				icon = ''
			case 2:
				color = 'blue'
				icon = 'bed'
			case 3:
				color = 'green'
				icon = 'cutlery'
		
		m2 = folium.Marker(location=[post.lat, post.lng], popup=popup, icon=folium.Icon(icon=icon, color=color, prefix='fa')) # 使用Font Awesome Icons
		m2.add_to(mCluster)
	
	folium.LayerControl().add_to(m)

	m=m._repr_html_()
	context = {'my_map': m, 'range': range(5,0,-1)}
	return render(request, 'home.html', context
		)

def area(request):
	url = request.build_absolute_uri()
	count = 0
	area_ID = ''
	d = False
	for s in url:
		if s == '=':
			d = True
		elif s.isdigit() and d == True:
			area_ID+=str(s)
		count+=1
	post = Post.objects.filter(area=area_ID).order_by('-created_date')
	AREA_CHOICES=((1,'基隆市'),
		(2,'台北市'),
		(3,'新北市'),
		(4,'桃園市'),
		(5,'新竹縣'),
		(6, '新竹市'),
		(7, '苗栗縣'),
		(8, '南投縣'),
		(9, '台中市'),
		(10, '彰化縣'),
		(11, '雲林縣'),
		(12, '嘉義縣'),
		(13, '嘉義市'),
		(14, '台南市'),
		(15, '高雄市'),
		(16, '屏東縣'),
		(17, '台東縣'),
		(18, '宜蘭縣'),
		(19, '花蓮縣'),
		(20, '澎湖縣'),	
		(21, '金門縣'),
		(22, '連江縣'),)
	area_title = AREA_CHOICES[int(area_ID)-1][1]
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'area.html', {'post_list': post_list,'area_title':area_title, 'user':user, 'range': range(5,0,-1)})

def attraction(request):
	post = Post.objects.filter(category=1).order_by('-created_date')
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'attraction.html', {
		'post_list': post_list,
		'user':user,
		'range': range(5,0,-1)
		})

def accomodation(request):
	post = Post.objects.filter(category=2).order_by('-created_date')
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'accomodation.html', {
		'post_list': post_list,
		'user':user,
		'range': range(5,0,-1)
		})


def restaurant(request):
	post = Post.objects.filter(category=3).order_by('-created_date')
	user = request.user
	art_comment = []
	for po in post:
		if po.comment_set.all():
			art_comment.append(po.comment_set.all())
		else:
			art_comment.append([])
	post_list = zip(post, art_comment)
	comment_form = post_comment_form()
	return render(request, 'restaurant.html', {
		'post_list': post_list,
		'user':user,
		'range': range(5,0,-1)
		})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post.html', {'post':post, 'range': range(1,6)})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			if post.photo:
				#print(post.photo,post.photo.url,post.photo.path)
				PATH = post.photo.path #A Filepath to an image on your computer"
				title = post.title
				print(CLIENT_ID)
				uploaded_image = im.upload_image(PATH, title=title)
				
				print(uploaded_image.title)
				print(uploaded_image.link)
				print(uploaded_image.type)
				post.imgur_url = uploaded_image.link
				post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form':form})

def post_delete(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('/')

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form})

def login(request):
	if request.user.is_authenticated:
		return redirect('/home/')
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return redirect('/home/')
	else:
		return render(request, 'login.html', locals())

def logout(request):
	auth.logout(request)
	return redirect('/home/')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'registration/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form':form}
		return render(request, 'registration/register.html', context)

def like_post(request):
	user = request.user
	if request.method == 'POST':
		pk = request.POST.get('post_pk')
		post = Post.objects.get(pk=pk)

		if user in post.liked.all():
			post.liked.remove(user)
		else:
			post.liked.add(user)

	return HttpResponse()

def post_serialized_view(request):
	data = list(Post.objects.values())
	return JsonResponse(data, safe=False)

def post_new_comment(request, post_id): 
	the_post = Post.objects.get(pk=post_id)
	if request.method =="POST":
		comment_form = post_comment_form(request.POST or None)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.comment_post = the_post
			new_comment.save()
			messages.success(request, "成功新增留言")
			return redirect('/attraction')
		else:
			return redirect('/attraction')