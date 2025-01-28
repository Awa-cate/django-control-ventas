from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Products, Sells
from datetime import date
from django.db.models import Sum


# Create your views here.
def all(request):
    
    if request.method == 'GET':
        hoy = date.today()
        total_importe = Sells.objects.filter(day=hoy).aggregate(Sum('total_import'))['total_import__sum']
        total_importe_mes = Sells.objects.filter(day__year=hoy.year, day__month=hoy.month).aggregate(Sum('total_import'))['total_import__sum'] or 0
        ventas_mes = Sells.objects.filter(day__year=hoy.year, day__month=hoy.month)
        
        all_products = Products.objects.all()
        ventas_hoy = Sells.objects.filter(day=hoy)
        
        all_sells = Sells.objects.all()
        return render(request, 'all.html', {
            'ventas': ventas_hoy,
            'total_importe': total_importe,
            'ventas_mes': ventas_mes,
            'total_importe_mes': total_importe_mes,
            'form': ProductForm,
            'sellForm': SellForm,
            'products': all_products,
            'sells': all_sells
        })
    else:
        if 'product_form' in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.save()
            else:
                return render(request, 'product.html'), {
                    'form': form,
                    'sellForm': SellForm(),
                    'products': Products.objects.all(),
                    'sells': Sells.objects.all(),
                }
        elif 'sell_form' in request.POST:
            sellsform = SellForm(request.POST)
            if sellsform.is_valid():
                new_sell = sellsform.save(commit=False)
                new_sell.save()
            else:
                return render(request, 'product.html'), {
                    'form': ProductForm(),
                    'sellForm': sellsform,
                    'products': Products.objects.all(),
                    'sells': Sells.objects.all()
                }
    
        return redirect('all')

def product(request):
    if request.method == 'GET':
        all_products = Products.objects.all()
        return render(request, 'product.html', {
            'form': ProductForm,
            'products': all_products,
        })

def product_detail(request, product_id):
    if request.method == 'GET':
        all_products = Products.objects.all()
        product = get_object_or_404(Products, pk=product_id)
        form = ProductForm(instance=product)
        return render(request, 'product_detail.html', {'product': product, 'form': form, 'all_products': all_products})
    else:
        product = get_object_or_404(Products, pk=product_id)
        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect('all')
    
def delete_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('all')

def sells(request):
    if request.method == 'GET':
        all_sells = Sells.objects.all()
        hoy = date.today()
        total_importe = Sells.objects.filter(day=hoy).aggregate(Sum('total_import'))['total_import__sum']
        total_importe_mes = Sells.objects.filter(day__year=hoy.year, day__month=hoy.month).aggregate(Sum('total_import'))['total_import__sum'] or 0
        return render(request, 'sells.html', {
            'sellForm': SellForm,
            'sells': all_sells,
            'total_importe': total_importe,
            'total_importe_mes': total_importe_mes
        })
  
def sells_detail(request, sell_id):
    if request.method == 'GET':
        all_sells = Sells.objects.all()
        sell = get_object_or_404(Sells, pk=sell_id)
        form = SellForm(instance=sell)
        return render(request, 'sells_detail.html', {'sells': sell, 'form': form, 'all_sells': all_sells})
    else:
        sell = get_object_or_404(Sells, pk=sell_id)
        form = SellForm(request.POST, instance=sell)
        form.save()
        return redirect('all')
    
def delete_sell(request, sell_id):
    sell = get_object_or_404(Sells, pk=sell_id)
    if request.method == 'POST':
        sell.delete()
        return redirect('all')
    
def forms(request):
    if request.method == 'GET':
        return render(request, 'forms.html', {
            'form': ProductForm,
            'sellForm': SellForm
        })