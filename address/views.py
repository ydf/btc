#-*-coding=utf-8-*-

import random
import hashlib

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


def address(request):
    pri_key = request.GET.get('pri_key')
    if not pri_key:
        pri_key = ''
        for i in range(1, 1500):
            pri_key += str(random.random()*1000000)
        print pri_key
        pri_key = hashlib.sha256(pri_key).hexdigest()
    #return render_to_response('/template/address.html',{'pri_key':pri_key, 'pub_key':pub_key})
    print pri_key
