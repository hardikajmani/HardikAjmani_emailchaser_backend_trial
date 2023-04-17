from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    user = request.user
    context = {"username": user.username, "useremail": user.email}
    print(user.username)
    return render(request, "home.html", context)
