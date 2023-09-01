from django.shortcuts import render,redirect
from .models import Pizza,Order

# Create your views here.
def home(request):
    return render(request,'pizzas/home.html')

def pizzas(request):
    pizzas=Pizza.objects.all()
    
    context={
        'pizzas':pizzas
    }

    return render(request,'pizzas/pizzas.html',context)
from .forms import OrderForm
def order(request,pk):
    pizza=Pizza.objects.get(id=pk)
    form=OrderForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            order=form.save(commit=False)
            order.pizza=pizza
            order.user=request.user
            order.save()
            return redirect('home')

    context={
        'pizza':pizza,
        'form':form
    }
    return render(request,'pizzas/order.html',context)


def my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={
        'orders':orders,
        
    }
    return render(request,'pizzas/my_orders.html',context)

def update(request,pk):
    order = Order.objects.get(id=pk)
    pizza = Pizza.objects.get(id=order.pizza.id)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order.save()
            return redirect('myorders')
    context = {
        'pizza' : pizza,
        'form' : form
    }
   
    return render(request,'pizzas/update.html',context)



def delete(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()
    return redirect('myorders')
   
