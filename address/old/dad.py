from  key import *
import binascii


s='9E6C99F226A37C6AA6AA6B442B3D0B87071BD78B6530B57890F01BA02A9B4A4B' #.....16...
shex=binascii.unhexlify(s)
address=CECKey()
address.set_secretbytes(shex)
address.set_compressed(compressed=True)
pub = CPubKey(address.get_pubkey(), address)

print '....',pub, '\n',pub.encode('hex'),len(pub)
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


print hashpub,zuihou

b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
import binascii

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






print encode(zuihou)
