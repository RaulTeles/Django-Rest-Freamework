from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.http import Http404

def register_view(request):
    #pegando as informações de sessão da view register_create
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register_view.html',{
        'form': form
    })

#view criada para receber o POST do register_view
#não irá renderizar nada, apenas receber, ler os dados, registrar ou dar um erro
def register_create(request):
    if not request.POST:
        raise Http404()
    
    #salvando os dados do usuário na sessão
    POST = request.POST
    request.session['register_form_data'] = POST
    
    form = RegisterForm(POST)

    return redirect('authors:register')