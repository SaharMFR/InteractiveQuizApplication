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
    path('start-quiz/<int:id>', views.start_quiz, name='start-quiz'),
    path('quiz/<str:id>/<int:user_id>', views.quiz, name='quiz'),
    path('quiz-details/<str:quiz_id>/<int:user_id>', views.quiz_details, name='quiz-details'),
]