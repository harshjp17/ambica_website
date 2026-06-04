from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Order
import json

def home(request):
    return render(request, 'main/home.html', {'page': 'home'})

def services(request):
    return render(request, 'main/services.html', {'page': 'services'})

def about(request):
    return render(request, 'main/about.html', {'page': 'about'})

def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your enquiry has been submitted. We will contact you within 24 hours.')
            return redirect('contact')
    else:
        form = EnquiryForm()
    return render(request, 'main/contact.html', {'page': 'contact', 'form': form})



def orders_login(request):
    if request.user.is_authenticated:
        return redirect('orders')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('orders')
        else:
            error = 'Invalid username or password'
    return render(request, 'main/orders_login.html', {'error': error})

def orders_logout(request):
    logout(request)
    return redirect('orders_login')

@login_required
def orders_page(request):
    return render(request, 'main/orders.html')

@login_required
@require_http_methods(["GET"])
def orders_list(request):
    orders = Order.objects.all()
    data = []
    for o in orders:
        data.append({
            'id':           o.id,
            'orderNo':      o.order_no,
            'orderDate':    o.order_date,
            'customerName': o.customer_name,
            'location':     o.location,
            'rate':         str(o.rate or ''),
            'totalNos':     str(o.total_nos or ''),
            'totalWeight':  str(o.total_weight or ''),
            'totalPrice':   str(o.total_price or ''),
            'pricePerNos':  str(o.price_per_nos or ''),
            'lineItems':    o.line_items,
            'notes':        o.notes,
            'status':       o.status,
        })
    return JsonResponse({'orders': data})

@login_required
@require_http_methods(["POST"])
def orders_save(request):
    d = json.loads(request.body)
    oid = d.get('id')
    fields = dict(
        order_no      = d.get('orderNo'),
        order_date    = d.get('orderDate', ''),
        customer_name = d.get('customerName', ''),
        location      = d.get('location', ''),
        rate          = d.get('rate') or None,
        total_nos     = d.get('totalNos') or None,
        total_weight  = d.get('totalWeight') or None,
        total_price   = d.get('totalPrice') or None,
        price_per_nos = d.get('pricePerNos') or None,
        line_items    = d.get('lineItems', []),
        notes         = d.get('notes', ''),
        status        = d.get('status', 'pending'),
    )
    if oid:
        Order.objects.filter(id=oid).update(**fields)
        o = Order.objects.get(id=oid)
    else:
        o = Order.objects.create(**fields)
    return JsonResponse({'id': o.id})

@login_required
@require_http_methods(["POST"])
def orders_delete(request, order_id):
    Order.objects.filter(id=order_id).delete()
    return JsonResponse({'ok': True})

@login_required
@require_http_methods(["POST"])
def orders_status(request, order_id):
    o = Order.objects.get(id=order_id)
    o.status = 'completed' if o.status == 'pending' else 'pending'
    o.save()
    return JsonResponse({'status': o.status})

from django.contrib.auth.decorators import login_required

@login_required
def orders(request):
    return render(request, 'main/orders.html', {'page': 'orders'})