from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = "quiz"

urlpatterns = [
    #path('api/', views.multiple_choice_new.as_view()),
    path('add-questions/', views.add_question,name="add_question"),
    #path('all-questions/', views.quiz_page),
    #path('answer/', views.answer,name="answer"),
    path('quiz/', views.quiz,name="quiz"),
    path('quiz-answer/', views.customized_response),
    path('upload/',views.upload,name="upload"),
]



