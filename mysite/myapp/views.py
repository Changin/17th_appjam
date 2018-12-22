from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.db.models import Q

# Create your views here.
@login_required
def write(request):
	return render(request, 'myapp/write.html', {})

@login_required
def date(request): #일정
	return render(request, 'myapp/date-picker.html', {})

@login_required
def clock(request): #스톱워치
	return render(request, 'myapp/clock.html', {})

@login_required
def post(request): #게시물 댓글
	return render(request, 'myapp/post.html', {})

@login_required
def index(request, board_id):

	posts = []
	if(board_id != 0):
		board_name = Board.objects.get(id=board_id)
	else:
		board_name = Board.objects.get(id=1)

	posts = Post.objects.filter(category__category=board_name.category).order_by('-created_date')

	username = request.user.username
	
	boards = []
	board1 = Board.objects.filter(age=1)
	board2 = Board.objects.filter(age=2)
	board3 = Board.objects.filter(age=3)

	hashtags = Post.objects.exclude(
      Q(hashtag__isnull=True)|Q(hashtag='')
    ).values_list('hashtag', flat=True).distinct()
	
	age = request.user.age
	userage = ""
	if (age <= 16):
		userage = "#13-16세"
		boards = [board1, board2, board3]
	elif (age <= 19):
		userage = "#17-19세"
		boards = [board2, board3, board1]
	else:
		userage = "#20-24세"
		boards = [board3, board2, board1]

	context = {
		'username' : username, 
		'userage' : userage,
		'boards' : boards,
		'hashtags' : hashtags,
		'posts' : posts,
	}
	return render(request, 'myapp/main.html', context)

def register(request):
	return render(request, 'myapp/register.html', {})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/0')
    return render(request,'myapp/login.html')