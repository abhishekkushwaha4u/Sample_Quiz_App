from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Question
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "quiz/homepage.html")

def about(request):
    return HttpResponse("<h2>About page</h2>")

def add_question(request):
    if request.method=="GET":
        return HttpResponse("{{csrf_token}}<form method=POST action='/add-question/'> <input type='text' name='question' /> <button type='submit'>Submit</button>")
    '''question = request.POST.get("question")
    qno = request.POST.get("qno")
    answer = request.POST.get("answer")
    new_question = Question(question=question, answer=answer, question_number=qno)
    new_question.save()'''
    return HttpResponse("Success")

def display_question(request):
    questions = Question.objects.all()
    print(questions)
    context = {}
    for q in questions:
        context.update({q.question_number: q.question})
        print(q.question_number)
        print(q.question)
    print(context)
    return render(request, "quiz/display.html", {"context":context})

@csrf_exempt
def add_new_question(request):
    if request.method=="GET":
        return render(request, "quiz/question.html")
    else: 
        question = request.POST.get("question")
        qno = request.POST.get("qno")
        answer = request.POST.get("answer")
        new_question = Question(question=question, answer=answer, question_number=qno)
        new_question.save()
        return HttpResponse("Success")
@csrf_exempt
def answer_question(request):
    question = Question.objects.all()
    print(question)
    context = {}
    #k=Question.objects.get(question_number=2)
    print(" sample output ")
    #print(k)

    for q in question:
    
        context.update({q.question_number: q.question})
        #print(q.question_number)
        #print(q.question)
    print(context)
    return render(request, "quiz/main_quiz.html",{"context":context})

@csrf_exempt
def handle_answer(request):
    if request.method=="POST":
        for q in Question.objects.all():
            print(request.POST.get("answer-given{}".format(q.question_number)))
        return HttpResponse("success")
    else:
        return HttpResponse("fail")
            
    
