#-*-coding=utf-8-*-

import random
import hashlib
import time
import binascii

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from address.key import CECKey, CPubKey


def address(request):
    #pri = request.GET.get('pri')
    pri = 0
    a = time.time()
    if not pri:
        pri = ''
        for i in range(1, 2):
            pri += str(random.random()*1000000)
        print pri
        pri = hashlib.sha256(pri).hexdigest()
    #return render_to_response('/template/address.html',{'pri':pri, 'pub_key':pub_key})
    pri02 = str(pri)
    import copy 
    pri01 = copy.copy(pri02)
    pub03 = gen_pub01(pri01)
    return HttpResponse(pub03)



def gen_pub01(pkey):
    pkey = '108a41977ebe5a5801b73dca4eb5d735f58621b63c3729f6d284dc57d4902869'
    shex= pkey.decode('hex')
    addr = CECKey()
    addr.set_compressed(compressed=True)
    addr.set_secretbytes(shex)


    pub = CPubKey(addr.get_pubkey(), addr)

    sha256=hashlib.sha256(pub)
    h=hashlib.new('ripemd160')
    h.update(sha256.digest())

    hashpub='00'+h.hexdigest()

    hashpub2=binascii.unhexlify(hashpub)
    sig=hashlib.sha256(hashlib.sha256(hashpub2).digest()).digest()[:4]
    print 'sig is',sig.encode('hex')
    zuihou=hashpub2+sig
    return encode(zuihou)


b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def encode(b):
    """Encode bytes to a base58-encoded string"""

    # Convert big-endian bytes to integer
    n = int('0x0' + binascii.hexlify(b).decode('utf8'), 16)

    # Divide that integer into bas58
    res = []
    while n > 0:
        n, r = divmod (n, 58)
        res.append(b58_digits[r])
    res = ''.join(res[::-1])

    # Encode leading zeros as base58 zeros
    import sys
    czero = b'\x00'
    if sys.version > '3':
        # In Python3 indexing a bytes returns numbers, not characters.
        czero = 0
    pad = 0
    for c in b:
        if c == czero: pad += 1
        else: break
    return b58_digits[0] * pad + res

