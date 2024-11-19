# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        Product.objects.create(name=name, price=price, quantity=quantity)
        return redirect('product_list')
    return render(request, 'product_form.html')

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})
