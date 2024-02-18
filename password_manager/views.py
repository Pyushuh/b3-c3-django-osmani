from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
# password_manager/views.py
from django.shortcuts import render, redirect
from .models import Site
from .forms import SiteForm


@login_required(login_url='login')
def base(request):
    sites = Site.objects.all()
    return render(request, 'base.html', {'sites': sites})

@login_required(login_url='login')
def site_list(request):
    sites = Site.objects.all()
    return render(request, 'site_list.html', {'sites': sites})

@login_required(login_url='login')
def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_list')
    else:
        form = SiteForm()
    return render(request, 'add_site.html', {'form': form})

@login_required(login_url='login')
def edit_site(request, site_id):
    site = Site.objects.get(pk=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_list')
    else:
        form = SiteForm(instance=site)
    return render(request, 'edit_site.html', {'form': form, 'site': site})

@login_required(login_url='login')
def delete_site(request, site_id):
    site = Site.objects.get(pk=site_id)
    site.delete()
    return redirect('site_list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('site_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
