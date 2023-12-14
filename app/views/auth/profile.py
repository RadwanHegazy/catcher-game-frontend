from django.shortcuts import render, redirect
from app.request_manager import Action, User



def ProfileView (request) : 

    user = User(request=request)

    if not user.is_auth :
        return redirect('login')


    
    context = {
        'u' : user.information()
    }

    
    response = render(request,'main/profile.html',context)

    return response
