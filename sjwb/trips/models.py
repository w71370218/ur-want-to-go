from email.policy import default
from pyexpat import model
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Tag(models.Model):
	name = models.CharField(max_length=10)
	color = models.CharField(max_length=7, default='#ff0000')
	icon = models.CharField(max_length=100,null=True, blank=True)
	imgur_url = models.URLField(blank=True, null=True)
	# 讓它改成顯示名稱
	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
	title = models.CharField(max_length=200, help_text='<font color="red">*必填</font>')
	text = models.TextField(help_text='<font color="red">*必填</font>')

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
	area = models.IntegerField(choices=AREA_CHOICES, default=1)

	CHOICES=((1,'景點'),(2,'住宿'),(3,'餐廳'))
	category = models.IntegerField(choices=CHOICES, default=1)
	
	location = models.CharField(max_length=100, help_text='<font color="red">*必填</font>')
	phone_number = models.CharField(max_length=12,blank=True, null=True, help_text='類型是住宿或餐廳才要填')
	tags = models.ManyToManyField(Tag, through='Tag_post', default=None,blank=True)
	photo = models.ImageField(upload_to='img/',blank=True, null=True)
	imgur_url = models.URLField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True) 
	liked = models.ManyToManyField(User,default=None,blank=True)
	stars = models.IntegerField(max_length=1, default=1, help_text='<font color="red">*必填</font>',validators=[MaxValueValidator(5)])
	lat  = models.FloatField(default=1, help_text='<font color="red">*必填</font>')
	lng = models.FloatField(default=1, help_text='<font color="red">*必填</font>')
	visited = models.BooleanField(default=False, help_text='<font color="red">*必填</font>')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	@property
	def num_likes(self):
		return self.liked.all().count()
	

	def __str__(self):
		return self.title

'''
author 			作者
title			標題
text 			介紹景點的內容
area 			地區選擇
category		類別
location 		地點
phone_number 	電話
tag				標籤
photo			照片
created_date
published_date
'''

class Tag_post(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	order = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.post}_{self.order}_{self.tag}'
	
	class Meta:
		unique_together = [['post', 'tag']]
		ordering = ('-post','order',)
	

class Comment(models.Model):
	comment_post = models.ForeignKey('post', on_delete=models.CASCADE)
	comment_content = models.CharField(max_length = 150, null=False)
	comment_man = models.CharField(max_length = 25, default="訪客")
	comment_date = models.DateTimeField(null=False, default = timezone.now)
	def __str__(self):
		return str(self.comment_post)
	class Meta:
		db_table = 'post_comment'
		ordering = ('-comment_date',)