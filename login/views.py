from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')

@login_required
def user_page_view(request):
    return render(request, 'login/user_page.html')