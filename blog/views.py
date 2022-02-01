from django.shortcuts import render, redirect,  HttpResponse, get_object_or_404
from .models import Product

from django.http import Http404
# Create your views here.

from .forms import ProductForm, RawForm


def home(request, *args, **kwargs):
    # return HttpResponse("<h2>Hello home </h2>")
    return render(request, 'home.html', {})


def about(request, *args, **kwargs):
    mycontext = {
        'title': 'this is about us ',
        'This_is_true': True,
        'my_number': 123,
        'my_list': [3, 43, 'koko'],
        'my_html': '<h3>hello world</h3>'
    }
    return render(request, 'about.html', mycontext)


def social(request, *args, **kwargs):
    return HttpResponse("<h2>hello social</h2>")


# TODO  product function


def product_detail_view(request):
    obj = Product.objects.get(id=1)

    # context = {
    #     'title': 'hello',
    #     'description': 'hello desc'
    # }
    context = {
        'object': obj
    }
    return render(request, 'product/detail.html', {'object': object})


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'product/create.html', context)


# def product_create_view(request):
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)

#     context = {}
#     return render(request, 'product/create.html', context)


# def product_create_view(request):

#     # form = RawForm()
#     # if request.method == 'POST':
#     #     form = RawForm(request.POST)
#     #     if form.is_valid():
#     #         print(form.cleaned_data)
#     #         # Product.objects.create(**form.cleaned_data)
#     #     else:
#     #         print(form.errors)

#     # context = {
#     #     'form': form
#     # }
#     # return render(request, 'product/create.html', context)


def render_initial_data(request):
    initial_data = {
        "title": "my awesome title "
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,
                       initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'product/create.html', context)


def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {

        "object": obj
    }

    return render(request, 'product/detail.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {

        "object_list": queryset

    }
    return render(request, 'product/product_list.html', context)
