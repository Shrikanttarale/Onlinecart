from django.contrib.auth.middleware import AuthenticationMiddleware
import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

IGNORE_PATHS=[
    re.compile(url.lstrip("/")) for url in getattr(settings, 'LOGIN_REQUIRED_IGNOR_PATHS',[])
]

class LoginRequiredMiddleware(AuthenticationMiddleware):
    def process_view(self,request,view_func,*view_args,**view_kwargs):
        #import pdb;pdb.set_trace() # python django debuger
        if request.user.is_authenticated:
            #print("User is authenticated")
            return None
        if not request.user.is_authenticated:
            #print("User not authenticated")
            path=request.path_info.lstrip('/')
            if not any(m.match(path) for m in IGNORE_PATHS):

                return redirect('{}'.format(reverse('users:login')))
