from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    # user = User.objects.all().order_by('-date')
    return render(request , 'user/register.html',{"form":form})

