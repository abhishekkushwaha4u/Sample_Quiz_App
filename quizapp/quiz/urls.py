from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name="home-page"),
    path("about/", views.about, name="about-page"),
    path("add-question/", views.add_question),
    path("display-questions/", views.display_question),
    path("add-new-question/",views.add_new_question),
    path("main_quiz/",views.answer_question),
    path("answer/", views.handle_answer, name="handle-answer"),
]