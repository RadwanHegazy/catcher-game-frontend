from django.shortcuts import redirect



def LogoutView (request) : 
    respones = redirect('login')
    
    if 'user' in request.COOKIES : 
        respones.delete_cookie('user')

    return respones