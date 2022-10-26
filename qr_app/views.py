from cgi import test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Report
from django.http import Http404
from .forms import Report_form
from qr_app.models import Report
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@login_required
def saved(request):
    try:
        return render(request, 'saved.html')
    except Http404:
        return redirect(request, '404.',{
            'error':'La pagina que estas tratando de buscar no ha respondido'
        })


@login_required
def signout(request):
    logout(request)
    return redirect('index')


def info(request):
    return render(request, 'info.html')


def report_form(request):
    return render(request, 'form.html')


def default(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                "form": AuthenticationForm,
                "error": "Usuario o contraseña incorrectos."
            })

        login(request, user)
        return redirect(reverse('form', args=(user.username,)))

@login_required
def settings(request):
    return render(request, 'settings.html', {
        'form':AuthenticationForm
    })

# --CRUD--
@login_required
def delete_report(request, pk):
    report = Report.objects.get(pk=pk)
    report.delete()
    user = User.objects.get(username=pk)
    logout(request)
    user.delete()
    return redirect(request, 'index.html', 
    {'info':'La cuenta ha sido eliminada'
    })

def read_filter_report(request, pk):
    try:
        report = Report.objects.get(pk=pk)
        return render(request, 'qr.html', {'report': report})
    except Report.DoesNotExist:
        return render(request, '404.html', {
            'error': 'El codigo no esta registrado o ha sido eliminado'
        })

def read_report(request, pk):
    # Intentamos leer los datos en base a la primary key
    # En caso de no poder entonces mandamos un error 404
    try:
        report = Report.objects.get(pk=pk)
        return render(request, 'qr.html', {'report': report})
    except Report.DoesNotExist:
        return render(request, '404.html', {
            'error': 'El codigo no esta registrado o ha sido eliminado'
        })


@login_required
def update_report(request, pk):
    try:
        report = Report.objects.get(pk=pk)
        form = Report_form(
            request.POST or None,
            instance=report
        )
        if request.POST and form.is_valid():
            print(form)
            form.save()
            return redirect('saved')
        return render(request, 'form.html', {'form': form})
    except ObjectDoesNotExist:
        render(request, '404.html',{
            'error':'El codigo que buscas no existe'
        })
