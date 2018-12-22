from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	age = models.IntegerField(null=False, blank=False, default=0)

# 게시글 테이블
class Post(models.Model):
	author = models.ForeignKey('MyUser', on_delete=models.CASCADE) #작성자
	title = models.CharField(max_length=200) #제목
	category = models.ForeignKey('Board', on_delete=models.CASCADE) #카테고리
	hashtag = models.CharField(max_length=200)		#해시태그
	context = models.TextField()					#내용

	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()

class Schedule(models.Model):
	author = models.ForeignKey('MyUser', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	start_time = models.DateTimeField(default=timezone.now)
	end_time = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

class Board(models.Model):
	category = models.CharField(max_length=200, unique=True) #카테고리
	context = models.CharField(max_length=200) #게시판 설명
	age = models.IntegerField(null=False, default=0) #나이, 중딩은 1, 고딩은 2, 대딩은 3

	def __str__(self):
		return self.category