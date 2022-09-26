from django.shortcuts import render, redirect
from django.contrib import messages
import math
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .filters import *

# Create your views here.


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!!!!!')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered!!!!!')
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()
                return redirect('/')
        else:
            messages.info(request, "Password Not Matching!!!!!!!!")
            return redirect('/register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/')
    return render(request, 'index.html')


@login_required
def metric1(request):
    return render(request, '1.1.3.html')


@login_required
def metric2(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        metric = '1.2.1'
        file = request.POST['file1']
        remarks = request.POST['remarks']
        user = request.user
        metric2 = ((int(subject1) * 100) / int(subject2))
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric2, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric2)
        return redirect('/metric2')
    return render(request, '1.2.1.html')


@login_required
def metric4(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '1.2.3'
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric4')
    return render(request, '1.2.3.html')


def report(request, pk):
    unique = User.objects.get(id=pk)
    reports = unique.submission_set.all()
    context = {
        'reports': reports,
    }
    return render(request, 'report.html', context)


def submission(request):
    reports = Submission.objects.all().order_by('-date')

    myFilter = SubmissionFilter(request.GET, queryset=reports)
    reports = myFilter.qs

    context = {
        'reports': reports,
        'myFilter': myFilter,
    }
    return render(request, 'submission.html', context)


@login_required
def metric5(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        metric = '1.3.2'
        file = request.POST['file1']
        remarks = request.POST['remarks']
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric5')
    return render(request, '1.3.2.html')


@login_required
def metric3(request):
    return render(request, '1.2.2.html')


def metric6(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        metric = '1.3.3'
        file = request.POST['file1']
        remarks = request.POST['remarks']
        user = request.user
        metric2 = ((int(subject1) * 100) / int(subject2))
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric2, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric2)
        return redirect('/metric6')
    return render(request, '1.3.3.html')


def metric7(request):
    return render(request, '1.4.1.html')


def metric8(request):
    return render(request, '1.4.2.html')


def metric9(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '2.1.1'
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric9')
    return render(request, '2.1.1.html')


def metric10(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '2.1.2'
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric10')
    return render(request, '2.1.2.html')


def metric11(request):
    return render(request, '2.2.2.html')


def metric12(request):
    return render(request, '2.3.3.html')


def metric13(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '2.4.1'
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric13')
    return render(request, '2.4.1.html')


def metric14(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '2.4.2'
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric14')
    return render(request, '2.4.2.html')


def metric15(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '2.4.3'
        sol = ((int(subject1)*100) / int(subject2))
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=sol, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, sol)
        return redirect('/metric15')
    return render(request, '2.4.3.html')


def metric16(request):
    if request.method == 'POST':
        subject1 = request.POST['subject1']
        subject2 = request.POST['subject2']
        file = request.POST['file1']
        remarks = request.POST['remarks']
        metric = '2.6.3'
        sol = ((int(subject1)*100) / int(subject2))
        metric4 = sol/5
        user = request.user
        sub = Submission(subject1=subject1, subject2=subject2, metric=metric,
                         value=metric4, file=file, remarks=remarks, user=user)
        sub.save()
        messages.success(request, metric4)
        return redirect('/metric16')
    return render(request, '2.6.3.html')


def metric17(request):
    return render(request, '2.7.1.html')
