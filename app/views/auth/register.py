from django.shortcuts import render, redirect
from app.request_manager import Action

def RegisterView (request) : 

    context = {}
    if request.method == "POST" : 

        data = {
            'email' : request.POST['email'],
            'password' : request.POST['password'],
            'full_name' : request.POST['full_name'],
        }
        
        files = {}

        if 'picture' in request.FILES : 
            files['picture'] = request.FILES['picture']

        action = Action(url='account/register/').post_method(data=data,files=files)
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


    return render(request,'auth/register.html',context)