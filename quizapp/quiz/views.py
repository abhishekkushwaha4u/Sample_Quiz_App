from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Question,Improved_Questions
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "quiz/homepage.html")

def about(request):
    return HttpResponse("<h2>About page</h2>")

def add_question(request):
    if request.method=="GET":
        return HttpResponse("{{csrf_token}}<form method=POST action='/add-question/'> <input type='text' name='question' /> <button type='submit'>Submit</button>")
    question = request.POST.get("question")
    qno = request.POST.get("qno")
    answer = request.POST.get("answer")
    new_question = Question(question=question, answer=answer, question_number=qno)
    new_question.save()
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
        count = 0
        left = 0
        user_response = {}
        correct_answer = {}
        for q in Question.objects.all():
            qno = q.question_number
            correct_answer.update({qno : q.answer})
            user_response.update({qno : request.POST.get("answer-given{}".format(qno))})
        print(user_response)
        print("Correct-answers are :")
        print(correct_answer)
        for i in user_response:
            if user_response[i]==" ":
                left+=1
            elif user_response[i]==correct_answer[i]:
                count+=1
        print("No of Correct responses is : "+str(count))
        print("No of unattempts is : "+str(left))
        incorrect = count - left
        
        # return HttpResponse("Your score is : "+str(count))
        return render(request, "quiz/quiz_result.html", {"user_response":user_response, "count": count,"correct_answer": correct_answer,"left": left,"incorrect": incorrect})
    else:
        return HttpResponse("fail")


def add_new_multiple_choice_question(request):
    if request.method=="GET":
        return render(request, "quiz/question2.html")
    question = request.POST.get("question")
    qno = request.POST.get("qno")
    answer = request.POST.get("answer")
    option1 = request.POST.get("option1")
    option2 = request.POST.get("option2")
    option3 = request.POST.get("option3")
    option4 = request.POST.get("option4")
    new_question = Improved_Questions(question=question, answer=answer, question_number=qno,option1=option1,option2=option2,option3=option3,option4=option4)
    new_question.save()
    return HttpResponse("Success")


            
    
