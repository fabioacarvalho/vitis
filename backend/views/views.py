from django.shortcuts import render, redirect, get_object_or_404 as getor404
from django.apps import apps
from django.contrib import admin
import os
from importlib import import_module

from django.urls import reverse
from base.forms import *

# Import all views into folder views...
current_directory = os.path.dirname(__file__)
# directory_to_imports = os.path.join(current_directory, 'views')
for filename in os.listdir(current_directory):
    if filename.endswith('_views.py') and filename != '__init__.py':
        module_name = filename[:-3]
        module = import_module(f'views.{module_name}')


def dashboard(request):
    return render(request, 'dashboard.html', locals())


def changelist(request, app, model):
    c_app, c_model = (app, model)

    model = apps.get_model(app, model)
    title = model._meta.verbose_name_plural

    model_admin = admin.site._registry.get(model)
    if model_admin:
        list_display = model_admin.list_display
    else:
        list_display = None

    values = model.objects.all()

    return render(request, 'base/changelist.html', locals())


def changeform(request, app, model, pk=None):
    cmodel = apps.get_model(app, model)
    title = cmodel._meta.verbose_name_plural


    if request.method == 'POST':
        form = MenuForm(request.POST)

        if form.is_valid():
            value = form.save()
            return redirect(reverse('vitis:changeform-edit', args=(app, model, value.pk)))
    else:
        form = MenuForm()
        
    return render(request, 'base/changeform.html', locals())


def changeform_edit(request, app, model, pk):
    model = apps.get_model(app, model)
    title = model._meta.verbose_name_plural

    instance = getor404(model, pk=pk)

    form = MenuForm(instance=instance)

    return render(request, 'base/changeform.html', locals())
