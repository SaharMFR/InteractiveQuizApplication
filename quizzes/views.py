from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import LoginForm
from quizzes.models import QuizzesUser, Quiz, TakenQuizzes, Choice, Question
import random
import string


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      email = request.POST['email']
      password = request.POST['password']
      user = QuizzesUser.objects.filter(email=email, password=password)
      if user:
        return redirect(f'/home/{user[0].id}')
    context = {'error': 'Invalid email or password'}
    return render(request, 'login.html', context)
  else:
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def signup(request):
  if request.method == "POST":
    entered_username = request.POST['username']
    entered_email = request.POST['email']
    entered_password = request.POST['password']
    entered_confirm_password = request.POST['confirm_password']

    if entered_password != entered_confirm_password:
        context = {'error': 'Passwords do not match'}
        return render(request, 'signup.html', context)
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
  taken_quizzes = TakenQuizzes.objects.filter(user_id=id)
  created_quizzes = Quiz.objects.filter(creator_id=id)
  context = {'user': user,
             'taken_quizzes': taken_quizzes,
             'created_quizzes': created_quizzes}
  return render(request, 'profile.html', context)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def create_quiz(request, id):
  user = QuizzesUser.objects.get(id=id)
  if request.method == "POST":
    description = request.POST['description']
    generated_id = generate_random_string(6)
    nQuestions = int(request.POST['nQuestions'])
    duration = int(request.POST['duration'])
    full_mark = 0
    quiz = Quiz(id=generated_id, creator_id=id, description=description, n_questions=nQuestions, duration=duration, full_mark=full_mark)
    quiz.save()
    for i in range(1, nQuestions + 1):
      question_description = request.POST['question_' + str(i)]
      mark = int(request.POST['mark_' + str(i)])
      full_mark = full_mark + mark
      question = Question(description=question_description, mark=mark, quiz=quiz)
      nChoices = int(request.POST['nChoices_' + str(i)])
      answer = request.POST['answer_' + str(i)]
      question.right_answer = answer
      question.save()
      for j in range(1, nChoices + 1):
        choice = Choice(text=request.POST['choice_' + str(j) + '_for_' + str(i)], question=question)
        choice.save()
    quiz.full_mark = full_mark
    quiz.save()
    context = {'user': user, 'message': 'Quiz have been created successfully!'
                                        '  With ID : ' + str(generated_id)}
    return render(request, 'create_quiz.html', context)
  context = {'user': user}
  return render(request, 'create_quiz.html', context)


def start_quiz(request, id):
  user = QuizzesUser.objects.get(id=id)
  if request.method == "POST":
    quiz_id = request.POST['quiz_id']
    quiz = Quiz.objects.filter(id=quiz_id)
    taken_before = TakenQuizzes.objects.filter(quiz_id=quiz_id, user_id=id)
    if taken_before:
      context = {'user': user,
                 'error': 'You have already taken this quiz!'}
      return render(request, 'start_quiz.html', context)
    if quiz:
      return redirect(f'/quiz/{quiz_id}/{id}')
    context = {'user': user,
               'error': 'Quiz does not exist!'}
    return render(request, 'start_quiz.html', context)
  context = {'user': user}
  return render(request, 'start_quiz.html', context)


def quiz(request, id, user_id):
  quiz = Quiz.objects.get(id=id)
  user = QuizzesUser.objects.get(id=user_id)
  questions = Question.objects.filter(quiz=quiz)
  choices = Choice.objects.all()
  if request.method == 'POST':
    score = 0
    for question in questions:
      if str(question.right_answer).lower() == str(request.POST['question_' + str(question.id)]).lower():
        score += question.mark
    taken_quiz = TakenQuizzes(user_id=user, quiz_id=quiz, score=score)
    taken_quiz.save()
    return redirect(f'/profile/{user_id}')
  context = {'quiz': quiz,
             'user': user,
             'questions': questions,
             'choices': choices}
  return render(request, 'quiz.html', context)


def quiz_details(request, quiz_id, user_id, taken_flag):
  user = QuizzesUser.objects.get(id=user_id)
  quiz = Quiz.objects.get(id=quiz_id)
  questions = Question.objects.filter(quiz=quiz)
  choices = Choice.objects.all()
  grade = None
  percent = None
  if taken_flag == 'true':
    taken_quiz = TakenQuizzes.objects.get(user_id=user, quiz_id=quiz)
    grade = taken_quiz.score
    percent = (float(grade) / quiz.full_mark) * 100
  context = {'quiz': quiz,
             'user': user,
             'questions': questions,
             'choices': choices,
             'grade': grade,
             'percent': percent}
  return render(request, 'quiz_details.html', context)


def page_404(request):
  template = loader.get_template('404.html')
  return HttpResponse(template.render())
