from sqlite3 import IntegrityError
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

from base.models import Exercices



########## sign in ################
def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
            ...
        else:
            messages.error(request , "wrong username or password")
            return redirect('login')
            
    return render(request, "signin.html")


########### register ###########
def register(request):           

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        if len(username) == 0 or len(email) == 0 or len(password) == 0:
            messages.error(request , "all fileds must be filled")
            return redirect('register')
        
        if len(password) < 8:
            messages.error(request, 'password must contain at least 8 caracters')
            return redirect('register')

        if not User.objects.filter(username = username).exists():
            user = User.objects.create_user(username , email , password)
            user.save() 
            messages.success(request , "your profile has been created")
            return redirect('login')
        
        else:
            messages.error(request , "user exists")
            return redirect('register')

    return render(request, "register.html")


############ profile page render################
def profile(request):

     if request.user.is_authenticated is True:
        user_id = request.user.id
        exercices = Exercices.objects.filter(user_id = user_id)
        context = {'exercices' : exercices}
        return render(request , "profile.html" , context)


################ logout #######################
def user_logout(request):
    logout(request)
    return redirect('home')



########### Add new exercice ################
def add_exercice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        load = request.POST.get('load')
        reps = request.POST.get('reps')

        if len(title) == 0 or len(load) == 0 or len(reps) == 0:
            messages.error(request, "all fields must be filed")
            return redirect('profile')

        if request.user.is_authenticated is True:
            user_id = request.user.id
            my_exercice = Exercices.objects.create(user_id = user_id , ex_title = title , ex_load = load , ex_reps = reps )
            my_exercice.save()

            messages.success(request, "Exercice saved")
            return redirect('profile')


        return redirect('profile')

######## delete an exercice ##################
def delete_exercice(request , exo):
    
    Exercices.objects.filter(id = exo).delete()
    messages.success(request , "exercice deleted succssfuly") 
    return redirect('profile')


############### edit an exercice ################
def edit_exercice(request , edited):
     title = request.POST.get('edit_title')
     load = request.POST.get('edit_load')
     reps = request.POST.get('edit_reps')

     exercice =  Exercices.objects.get(id = edited)
     if len(title) > 0:
        exercice.ex_title = title
    
     if len(load) > 0:
        exercice.ex_load = load
     if len(reps) > 0:
        exercice.ex_reps = reps
     
     exercice.save()

     return redirect('profile')