from django.shortcuts import render, redirect
from app.request_manager import Action

def LoginView (request) : 

    context = {}
    if request.method == "POST" : 

        data = {
            'email' : request.POST['email'],
            'password' : request.POST['password']
        }

        action = Action(url='account/login/').post_method(data=data)
        status = action['status']
        response = action['data']
        
        is_ok = (status == 200)

        if not is_ok :
            context = response
        else:
            user = response['token']
            response = redirect('profile')
            response.set_cookie('user',user)
            return response


    return render(request,'auth/login.html',context)