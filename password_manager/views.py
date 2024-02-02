from django.shortcuts import render

# Create your views here.
# password_manager/views.py
from django.shortcuts import render, redirect
from .models import Site
from .forms import SiteForm


def base(request):
    sites = Site.objects.all()
    return render(request, 'base.html', {'sites': sites})


def site_list(request):
    sites = Site.objects.all()
    return render(request, 'site_list.html', {'sites': sites})


def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site_list')
    else:
        form = SiteForm()
    return render(request, 'add_site.html', {'form': form})


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


def delete_site(request, site_id):
    site = Site.objects.get(pk=site_id)
    site.delete()
    return redirect('site_list')
