from django.shortcuts import redirect, render
from app.request_manager import User, Action
from django.http import Http404



def BattleView(request,battleuuid) : 
    
    context = {}
    user = User(request)
    
    if not user.is_auth :
        return redirect('login')
    
    action = Action(url=f'battle/get/{battleuuid}/',token=request.COOKIES['user']).get_method()
    status = action['status']
    is_valid = (status == 200)

    data = action['data']

    if not is_valid or data['winner'] is not None :
        raise Http404(request)
    

    context = data
    
    context['uuid'] = battleuuid
    context['token'] = request.COOKIES['user']
    context['u'] = user.information()



    return render(request,'main/battle.html',context)