from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from accounts.forms import LoginForms


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muaffaqiyatli login qilindi')
                else:
                    return HttpResponse('Sizning profilingiz faol holatda emas')

            else:
                return HttpResponse('Login yoki Parolda hatolik bor')
    else:
        form = LoginForms()
        context = {
            'form': form
        }
        return render(request, 'registration/login.html', context=context)


def dashboard(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/dashboard.html', context=context)

