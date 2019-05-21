from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from Users.urls import *
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .models import multiple_choice
#from .serializers import multiple_choiceSerializer
import random
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage



# def home_page(request):
#     return render(request, "quiz/home.html")


# def about(request):
#     return HttpResponse("This is about page")

# # for QuizAPI


# class multiple_choice_new(APIView):
#     def get(self, request):
#         objects = multiple_choice.objects.all()
#         serializer = multiple_choiceSerializer(objects, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         objects = multiple_choice.objects.all()
#         serializer = multiple_choiceSerializer(objects, many=True)
#         return Response(serializer.data)
# To add new questions


def add_question(request):
    if request.method == "GET":
        return render(request, "quiz/question.html")
    else:
        objects = multiple_choice.objects.values_list('question_number', flat=True)
        if len(objects) == 0:
            q_no = 1
        else:
            q_no = list(objects)[-1]+1
        question = request.POST.get("question")
        answer = request.POST.get("answer")
        a = request.POST.get("a")
        b = request.POST.get("b")
        c = request.POST.get("c")
        d = request.POST.get("d")
        new_question = multiple_choice(
            question=question, answer=answer, question_number=q_no, a=a, b=b, c=c, d=d)
        new_question.save()
        return HttpResponse("Success")

@login_required()
def quiz_page(request):
    question = multiple_choice.objects.all()
    context = []

    for q in question:
        context.append({"question_number": q.question_number,
                        "question": q.question, "a": q.a, "b": q.b, "c": q.c, "d": q.d})
    print(context)
    return render(request, "quiz/quiz_page.html", {"context": context})


@login_required()
def answer(request):
    if request.method == "POST":
        score = 0
        L = dict(request.POST)
        if 'A' not in L:
            A = []
        else:
            A = map(int, L['A'])
        if 'B' not in L:
            B = []
        else:
            B = map(int, L['B'])
        if 'C' not in L:
            C = []
        else:
            C = map(int, L['C'])
        if 'D' not in L:
            D = []
        else:
            D = map(int, L['D'])

        Q = multiple_choice.objects.all()
        M = dict(zip([i for i in range(1, Q[len(Q)-1].question_number+1)], [[]for i in range(1, Q[len(Q)-1].question_number+1)]))
        print(M)
        for i in A:
            M[i].append('A')
        for i in B:
            M[i].append('B')
        for i in C:
            M[i].append('C')
        for i in D:
            M[i].append('D')
        print(M)
        print([i.answer for i in Q])
        for i in Q:
            if M[i.question_number] == []:
                print("You did not attempt question number {}".format(
                    i.question_number))
                pass
            elif len(i.answer.split(',')) == len(M[i.question_number]):
                if list(i.answer.split(',')) == M[i.question_number]:
                    print("You scored +4 for correct entries")
                    score += 4
                else:
                    print(
                        "You scored -1 for incorrect entries with partial or no options correct")
                    score -= 1
            elif len(i.answer.split(',')) > len(M[i.question_number]):
                for i1 in M[i.question_number]:
                    if i1 not in i.answer.split(','):
                        score -= 1
                        print(
                            "You entered an incorrect entry out of the total options entered!")
                        break
                    else:
                        pass
                    print("You got partial marking of {} options out of {} options in this question".format(
                        len(M[i.question_number]), len(i.answer.split(','))))
                    score += len(M[i.question_number])
            else:
                print("You got negative marking!")
                score -= 1
        return HttpResponse("Done! Your score is "+str(score))
    else:
        return HttpResponse("Access Restricted!")


@login_required()
def quiz(request):
    if request.method == "GET":
        return render(request, "temp/temporary.html")
    else:
        n = int(request.POST.get("no-of-questions"))
        p = len(multiple_choice.objects.all())
        if n > p:
            return HttpResponse('<html><head><body>Do not have enough questions in database! Enter lesser no of questions!<a href="/quiz/quiz/">Click here</a></body></head></html>')
        L = random.sample(range(1, p+1), n)
        return(customized_questions(request, L))


@login_required()
def customized_questions(request, L):
    context = []
    n = 1
    for i in L:
        q = multiple_choice.objects.get(id=i)
        context.append({"id": q.id, "question_number": n,
                        "question": q.question, "a": q.a, "b": q.b, "c": q.c, "d": q.d})
        n += 1
    #print(context)
    return render(request, "temp/quiz_page.html", {"context": context})


@login_required()
def customized_response(request):
    print(dict(request.POST))
    L = dict(request.POST)
    if 'A' in L:
        A = list(map(int, L['A']))
    else:
        A = []
    if 'B' in L:
        B = list(map(int, L['B']))
    else:
        B = []
    if 'C' in L:
        C = list(map(int, L['C']))
    else:
        C = []
    if 'D' in L:
        D = list(map(int, L['D']))
    else:
        D = []

    R = []
    R.extend(A)
    R.extend(B)
    R.extend(C)
    R.extend(D)
    R = list(set(R))

    print(R)
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("D:", D)
    M = defaultdict(list)
    Q = {}
    for i in R:
        correct = multiple_choice.objects.get(id=int(i))
        Q[i] = (correct.answer).split(',')
    for i in A:
        M[i].append('A')
    for i in B:
        M[i].append('B')
    for i in C:
        M[i].append('C')
    for i in D:
        M[i].append('D')
    # print(M)
    # print(Q)
    score = 0
    count = 1
    for i in Q:
        if M[i] == []:
            print("You did not attempt question number {}".format(count))
        elif len(Q[i]) == len(M[i]):
            if Q[i] == M[i]:
                print("You scored +4 for correct entries")
                score += 4
            else:
                print(
                    "You scored -1 for incorrect entries with partial or no options correct")
                score -= 1
        elif len(Q[i]) > len(M[i]):
            for i1 in M[i.question_number]:
                if i1 not in i.answer.split(','):
                    score -= 1
                    print(
                        "You entered an incorrect entry out of the total options entered!")
                    break
                else:
                    pass
                print("You got partial marking of {} options out of {} options in this question".format(
                    len(M[i.question_number]), len(i.answer.split(','))))
                score += len(M[i.question_number])
        else:
            print("You got negative marking!")
            score -= 1
        count += 1
    return HttpResponse("Done! Your score is "+str(score))

@login_required()
def upload(request):
    if request.method=="POST":
        file = request.FILES["document"]
        k = file.name.split('.')
        if file.size > 10000000:
            return HttpResponse("file size exceeded! Enter less than 10 mb")
        elif 'csv' not in k:
            return HttpResponse("only csv file accepted!")
        else:
            fs = FileSystemStorage()
            fs.save(file.name,file)
            return HttpResponse("File uploaded!")
    else:
        return render(request,"quiz/upload.html")







    
