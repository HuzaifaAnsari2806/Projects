from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.contrib.auth import authenticate, login
from django.urls import reverse


from .forms import RecipeForm, RecipeIngredientForm, RecipeIngredientImageForm
from .models import Recipe, RecipeIngredient, RecipeIngredientImage
# Create your views here.


@login_required
def list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "objects_list": qs
    }
    return render(request, "recipe/list.html", context)


@login_required
def detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        "object": obj
    }
    return render(request, "recipe/detail.html", context)


@login_required
def create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "recipe/create-update.html", context)


@login_required
def update_view(request, id):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    try:
        obj1 = get_object_or_404(RecipeIngredient, recipe__id=id, recipe__user=request.user)
    except RecipeIngredient.MultipleObjectsReturned:
        obj1 = RecipeIngredient.objects.filter(recipe__id=id, recipe__user=request.user).first()

    form = RecipeForm(request.POST or None, instance=obj)
    RecipeIngredientFormset = modelformset_factory(
        RecipeIngredient, form=RecipeIngredientForm, extra=0)
    qs = obj.recipeingredient_set.all()
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)
    context = {
        "form": form,
        "object": obj,
        "object1":obj1,
        "formset": formset
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for forms in formset:
            child = forms.save(commit=False)
            # if child.recipe is None:
            child.recipe = parent
            child.save()

        context["message"] = "Data Saved."
        # return redirect(obj.get_absolute_url())
    return render(request, "recipe/create-update.html", context)


@login_required
def delete_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    if request.method == 'POST':
        obj.delete()
        success_url = reverse('recipes:list')
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "recipe/delete.html", context)


@login_required
def recipe_ingredient_delete_view(request, parent_id=None, id=None):
    obj = get_object_or_404(
        RecipeIngredient, recipe__id=parent_id, id=id, recipe__user=request.user)
    if request.method == 'POST':
        obj.delete()
        success_url = reverse('recipes:detail', kwargs={'id': id})
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "recipe/delete.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "Invalid credentials"}
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('/pantry/recipes')
    return render(request, 'login.html', {})


def recipe_ingredient_image_view(request, parent_id=None):
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        raise Http404
    form = RecipeIngredientImageForm(
        request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.recipe_id = parent_obj.id
        obj.save()
    return render(request, 'recipe/image-form.html', {'form': form,'object':parent_obj})
