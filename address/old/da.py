from  key import *

def gen_pub(pri_key, compressed=True):
    import copy
    data = copy.deepcopy(pri_key)
    shex= data.decode('hex')
    addr = CECKey()
    addr.set_secretbytes(shex)
    addr.set_compressed(compressed=True)
    pub = CPubKey(addr.get_pubkey(), addr)


    import hashlib
    sha256=hashlib.sha256(pub)
    h=hashlib.new('ripemd160')
    h.update(sha256.digest())
    print h.hexdigest()

    hashpub='00'+h.hexdigest()
    import binascii
    hashpub2=binascii.unhexlify(hashpub)
    sig=hashlib.sha256(hashlib.sha256(hashpub2).digest()).digest()[:4]
    print 'sig is',sig.encode('hex')
    zuihou=hashpub2+sig

    #return encode(zuihou)

pri_key = '9b3230f8fc95bde46c2a6f3324cafe88b879823b9c36f3e342e9b341f8e2b2e5'
gen_pub(pri_key)