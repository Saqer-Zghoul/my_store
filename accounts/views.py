from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from orders.models import Order

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول تلقائياً بعد التسجيل
            return redirect('products:product_list')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    # جلب الطلبات الخاصة بالمستخدم المادي الحالي
    user_orders = Order.objects.filter(email=request.user.email)
    return render(request, 'accounts/profile.html', {'orders': user_orders})