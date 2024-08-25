from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/<int:id>', views.home, name='home'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('new-quiz/<int:id>', views.create_quiz, name='new-quiz'),
    path('start-quiz/', views.start_quiz, name='start-quiz'),
    path('quiz/<int:id>/<int:user_id>', views.quiz, name='quiz'),
]