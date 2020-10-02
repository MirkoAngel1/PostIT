# auth es para logear # udpdate es para aulo login despues del cambio de pass
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# decorador para que sea necesario loguin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # trae el modelo de usuario
# 2 tipos de respues hacia templates
from django.shortcuts import redirect, render
# robado de django para cambiar pass
from django.contrib.auth.forms import PasswordChangeForm

# tre los forms de la otra app
from apps.user.forms import LoginForm, registernota, registerUser
from apps.user.models import nota  # trae los model de la otra app
from apps.user.views import mostrar_notas  # tra el mostrar_notas de la otra app

from .forms import changeUsernameForm, changeEmailForm  # tra los form de esta app
from django.contrib import messages  # para mostrar mensajes


def indexPage(request):
    if request.method == "POST":
        # trae el formulario Loginform desde el template
        log_in = LoginForm(request.POST)
        model_username = request.POST.get('username')  # trae el campo
        model_password = request.POST.get('password')
        if (model_username != None) and (model_password != None):  # pregunta se no son vacios
            try:  # solo trata el error de contraseña
                if log_in.is_valid():  # verifica el formulario traido con respecto al modelo en forms.py
                    user = authenticate(username=model_username,
                                        password=model_password)  # logea
                    login(request, user)  # este lo agrega al request
                    # mensaje de usuario logeado
                    messages.success(request, 'User name is: '+model_username)
                    current_user = request.user  # trae de la request el usuario actual logeado
                    # trae de la base de datos el usuario
                    user = User.objects.get(username=model_username)
                    if login:  # si loguin es correcto
                        # direcciona a la funcion
                        return mostrar_notas(request)
                    else:
                        return redirect('index')  # direcciona al index
                else:
                    # mensaje de no validado
                    messages.success(request, 'data error :')
                    return redirect('index')
            except AttributeError:
                return redirect('index')
            else:
                return redirect('index')
    # trae el form registre user del template
    newUser = registerUser(request.POST)
    model = User  # tra el molde User
    if newUser.is_valid():  # valida el formulario
        # limpia el username que es afectado al validar
        model.username = newUser.cleaned_data["username"]
        model.email = newUser.cleaned_data["email"]
        model.password1 = newUser.cleaned_data["password1"]
        model.password2 = newUser.cleaned_data["password2"]
        if (type(model.password1) != int) and (model.password1 != model.email) and (model.password1 != model.username) and (len(model.password1) > 7) and (model.password1 == model.password2):  # verifica la contraseña
            grabar = User(username=model.username, email=model.email,
                          password=model.password1)  # instancia un User
            grabar.save()  # graba
            # busca en la base de datos el useario recien registrado
            user = User.objects.get(username=model.username)
            user.is_staff = True  # lo agrega como usuario staff
            user.is_active = True  # lo agrega como usuario activo
            user.set_password(model.password1)  # codifica el pass
            user.save()  # graba las lineas anteriores
            messages.success(
                request, 'New user create whit name '+model.username)  # mensaje de usuario creado
            # envia al index
            return render(request, 'login/index.html', {'newUser': newUser, "log_in": log_in})
        else:
            print("error en el formulario")  # error en la contraseña
    else:
        newUser = registerUser()  # envia el formulario de forms.py al template
        log_in = LoginForm()  # envia el formulario login  de forms.py al template
        # recarga index
        return render(request, 'login/index.html', {'newUser': newUser, "log_in": log_in})


@login_required
def logoutUser(request):
    logout(request)  # deslogea
    return redirect('index')


@login_required
def settingsUser(request):
    current_user = request.user  # trae el usuario logueado desde el request
    # busca los datos del usuario en la base de datos
    user = User.objects.get(id=current_user.id)
    ctx = {"user": user}  # contexto
    return render(request, 'login/settings.html', ctx)


@login_required
def changeEmail(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changeEmailForm(request.POST)
        model_email = request.POST.get("email")
        model_email2 = request.POST.get('email2')
        model_email3 = request.POST.get('email3')
        if model_email == user.email:
            grabar = User(id=user.id, username=user.username, email=model_email2,
                          password=user.password)
            if (model_email != (model_email2 == model_email3)):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.save()
                username = user.username
                password = user.password
                user = authenticate(
                    request, username=username, password=password)
                if user:
                    login(request, user)
                    return mostrar_notas(request)
                return redirect('home')
            else:
                return redirect('changeEmail')
        else:
            return redirect('changeEmail')
    else:
        newUser = changeEmailForm()
    return render(request, "login/changeEmail.html", {'User': newUser})


@login_required
def changePass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            print('Your password was successfully updated!')
            return redirect('home')
        else:
            print('Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login/changePass.html', {
        'form': form
    })


@login_required
def changeUsername(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changeUsernameForm(request.POST)
        model_username = request.POST.get("username")
        model_username2 = request.POST.get('username2')
        model_username3 = request.POST.get('username3')
        if model_username == user.username:
            grabar = User(id=user.id, username=model_username2, email=user.email,
                          password=user.password)
            if (model_username != (model_username2 == model_username3)):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.save()
                username = user.username
                password = user.password
                user = authenticate(
                    request, username=username, password=password)
                if user:
                    login(request, user)
                    return mostrar_notas(request)
                return redirect('home')
            else:
                print("username no coincide o es igual al viejo")
                return redirect('changeUsername')
        else:
            print("formulario invalido")
            return redirect('changeUsername')
    else:
        newUser = changeUsernameForm()
    return render(request, "login/changeUsername.html", {'User': newUser})
