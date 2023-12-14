from django.shortcuts import redirect, render
from app.request_manager import User, Action
from django.http import Http404



def WinnerView(request,battleuuid) : 
    
    context = {}
    user = User(request)
    
    if not user.is_auth :
        return redirect('login')
    
    action = Action(url=f'battle/get/{battleuuid}/',token=request.COOKIES['user']).get_method()
    status = action['status']
    is_valid = (status == 200)

    if not is_valid :
        raise Http404(request)
    
    winner = action['data']['winner']
    data = action['data']

    context = data
    
    if winner == 'red' :
        winner_user = action['data']['red_player']
    else:
        winner_user = action['data']['blue_player']

    context['winner'] = winner_user

    return render(request,'main/winner.html',context)