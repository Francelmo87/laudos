from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Client


@login_required
def main(request):
    client = Client.objects.filter(active=True, user=request.user)
    return render(request, 'main.html', {'client': client})


def logout(request):
    return redirect(request, 'registration/login.html')
