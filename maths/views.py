from django.shortcuts import render, redirect
from django.contrib import messages
import math
# Create your views here.


def home(request):
    return render(request, 'index.html')


def percentage(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        subject3 = request.POST['subject3']
        subject4 = request.POST['subject4']
        subject5 = request.POST['subject5']
        percentage = (int(subject1)+int(subject1) +
                      int(subject1)+int(subject1)+int(subject1))/5
        messages.success(request, percentage, '%')
        return redirect('/percentage')
    return render(request, 'percentage.html')


def average(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        subject3 = request.POST['subject3']
        subject4 = request.POST['subject4']
        subject5 = request.POST['subject5']
        average = (int(subject1)+int(subject1) +
                   int(subject1)+int(subject1)+int(subject1))/5
        messages.success(request, average)
        return redirect('/average')
    return render(request, 'average.html')


def square_root(request):
    if request.method == 'POST':
        number = request.POST['number']
        number = int(number)
        square_root = math.sqrt(number)
        messages.success(request, square_root)
        return redirect('/square_root')
    return render(request, 'square_root.html')


def simple_interest(request):
    if request.method == 'POST':
        principal = request.POST['principal']
        rate = request.POST['rate']
        time = request.POST['time']
        si = (float(principal)*float(rate)*float(time))/100
        messages.success(request, si)
        return redirect('/simple_interest')
    return render(request, 'simple_interest.html')


def quadratic_equation(request):
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        a = float(a)
        b = float(b)
        c = float(c)
        d = b**2-4*a*c
        if (d < 0):
            messages.success(request, 'This equation has no real solution')
        elif(d == 0):
            x = (-b+math.sqrt(d))/2*a
            messages.success(request, x)
        else:
            x1 = (-b+math.sqrt(d))/2*a
            x2 = (-b-math.sqrt(d))/2*a
            messages.success(request, x1)
            messages.success(request, x2)
        return redirect('/quadratic_equation')
    return render(request, 'quadratic_equation.html')
