'''
Verify the signature of the session key of consumer
'''
import ecdsa
from ecdsa.ecdsa import curve_secp256k1
from ecdsa.util import randrange
from ecdsa.curves import SECP256k1
import utils
import pickle

# load the masked public key list from ./key_pairs/mask_i.txt
def read_masked_public_key_list(number_participants):
    masked_public_key_list = []
    for i in range(number_participants):
        with open('./key_pairs/mask_' + str(i) + '.txt', 'r') as f:
            x, y = f.read().split(' ')
            masked_public_key_list.append(ecdsa.ellipticcurve.Point(curve_secp256k1, int(x), int(y)))
    return masked_public_key_list

# load the mask from ./key_pairs/mask_M.txt
def read_mask():
    with open('./key_pairs/mask_M.txt', 'r') as f:
        x, y = f.read().split(' ')
        _M = ecdsa.ellipticcurve.Point(curve_secp256k1, int(x), int(y))
    return _M

# load signature from signature2.txt
def load_signature():
    with open('./signature.txt', 'rb') as f:
        signature = pickle.load(f)
    return signature

if __name__ == '__main__':
    masked_public_key_list = read_masked_public_key_list(10)
    _M = read_mask()
    signature = load_signature()
    session_key_signature = signature
    session_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsQZgKydNPkPVtvvqDfzCaIJVF
A1pLwQraRDOunZ6iDq2h6Xzn5AriCWCxe4tXNYvHdQp07H89ySTmZHAFQDzx79Ip
76CDTkNG1bDzNFI3TYZNtn5TyGSetHPq9QNJaEzhH4YQtNjYzfO3Ex1SptaWjX/o
UdChSVRnxJ3+LPujnQIDAQAB
-----END PUBLIC KEY-----'''
    # verify the signature of the session key
    if utils.verify_ring_signature(session_key, masked_public_key_list, *session_key_signature, _M):
        print('The signature of the session key is valid.')
    else:
        print('The signature of the session key is invalid.')