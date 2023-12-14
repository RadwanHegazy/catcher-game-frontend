import requests
from frontend.settings import MAIN_URL
from django.shortcuts import redirect

class Action :

    def __init__(self, url, token=None) -> None:
        self.url = MAIN_URL + '/' + url
        self.token = token
        self.headers = {'Authorization':f'token {token}'}

    
    def get_method (self) : 
        
        if self.token  : 
            req = requests.get(self.url,headers=self.headers)
        else:
            req = requests.get(self.url)

        context = {
            'status' : req.status_code,
            'data' : req.json()
        }

        return context
    

    def post_method (self, data=None,files=None) : 

        if data is None : 
            data = {}
        
        if files is None : 
            files = {}

        if self.token  : 
            req = requests.post(self.url,headers=self.headers,data=data,files=files)
        else:
            req = requests.post(self.url,data=data,files=files)

        context = {
            'status' : req.status_code,
            'data' : req.json()
        }

        return context
    

class User :
    
    def __init__(self, request) :


        self.is_auth = False

        if 'user' in request.COOKIES :
            user = request.COOKIES['user']
            self.action = Action(url='account/profile/',token=user).get_method()
            
            status = self.action['status']
            is_ok = (status == 200)

            if is_ok : 
                self.is_auth = True
        




    def information (self) : 
        return self.action['data']
    

    
