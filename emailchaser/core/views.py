from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'home.html', context)