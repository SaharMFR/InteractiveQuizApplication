# # from tempfile import template
# # from unittest import loader
#
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import loader
#

#
#
# def index_page(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import LoginForm
# from sqlalchemy.testing.pickleable import User

from quizzes.models import QuizzesUser, Quiz, TakenQuizzes


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def login(request):
  # template = loader.get_template('login.html')
  # return HttpResponse(template.render())
  # print(request.method)
  if request.method == 'POST':
    # print("\nMethod is POST\n")
    form = LoginForm(request.POST)
    if form.is_valid():
      # print("Login form is valid")
      email = request.POST['email']
      password = request.POST['password']
      user = QuizzesUser.objects.get(email=email, password=password)
      if user:
        # print("User exists")
        # print(user.id)
        return redirect(f'/home/{user.id}')
    # print("User does not exist")
    context = {'error': 'Invalid email or password'}
    return render(request, 'login.html', context)
  else:
    form = LoginForm()
    context = {'form': form}
    # print("\nMethod is not POST\n")
    return render(request, 'login.html', context)
  # print("\nOutside if\n")
  # return redirect('login')

# def signup_page(request):
#   template = loader.get_template('signup.html')
#   return HttpResponse(template.render())

def signup(request):
  # template = loader.get_template('signup.html')

  if request.method == "POST":
    entered_username = request.POST['username']
    entered_email = request.POST['email']
    entered_password = request.POST['password']
    entered_confirm_password = request.POST['confirm_password']

    if entered_password != entered_confirm_password:
        context = {'error': 'Passwords do not match'}
        return render(request, 'signup.html', context)
    # existing_user = QuizzesUser.objects.filter(username=entered_username)
    # if existing_user:
    #   context = {'error': 'Username already taken!'}
    #   return HttpResponse(template.render(request, context))
    existing_user = QuizzesUser.objects.filter(email=entered_email)
    if existing_user:
      context = {'error': 'Email already taken!'}
      return render(request, 'signup.html', context)
    new_user = QuizzesUser(username=entered_username, email=entered_email, password=entered_password)
    new_user.save()
    return redirect('/login/')
  return render(request, 'signup.html')

def home(request, id):
  user = QuizzesUser.objects.get(id=id)
  context = {'user': user}
  return render(request, 'home.html', context)

def profile(request, id):
  user = QuizzesUser.objects.get(id=id)
  # taken_quizzes_table = QuizzesUser.taken_quizzes.through
  taken_quizzes = TakenQuizzes.objects.filter(user_id=id)
  created_quizzes = Quiz.objects.filter(creator_id=id)
  context = {'user': user,
             'taken_quizzes': taken_quizzes,
             'created_quizzes': created_quizzes}
  return render(request, 'profile.html', context)

def create_quiz(request, id):
  user = QuizzesUser.objects.get(id=id)
  context = {'user': user}
  return render(request, 'create_quiz.html', context)

def start_quiz(request):
  template = loader.get_template('start_quiz.html')
  return HttpResponse(template.render())

def quiz(request, id):
  quiz = QuizzesUser.objects.get(id=id)
  context = {'quiz': quiz,
             'creator': quiz.creator_id}
  return render(request, 'quiz.html', context)

def page_404(request):
  template = loader.get_template('404.html')
  return HttpResponse(template.render())
