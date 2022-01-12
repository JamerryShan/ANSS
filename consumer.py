"""
Consumer will read the masked public key list from the files
Sign its own session key via the group signature using its private key
"""

import utils
import ecdsa
from ecdsa.ecdsa import curve_secp256k1
import pickle

# Read the masked public key list from ./key_pairs/mask_i.txt
# the public key is stored in the form of two strings split by a space
# convert the two strings to Point object
def read_masked_public_key_list(number_participants):
    masked_public_key_list = []
    for i in range(number_participants):
        with open('./key_pairs/mask_' + str(i) + '.txt', 'r') as f:
            x, y = f.read().split(' ')
            masked_public_key_list.append(ecdsa.ellipticcurve.Point(curve_secp256k1, int(x), int(y)))
    return masked_public_key_list

# read the private key from ./key_pairs/private_key_i.txt
def read_private_key(index):
    with open('./key_pairs/private_key_' + str(index) + '.txt', 'r') as f:
        private_key = int(f.read())
    return private_key

if __name__ == '__main__':
    index = 2
    # read the masked M from ./key_pairs/mask_M.txt
    with open('./key_pairs/mask_M.txt', 'r') as f:
        x, y = f.read().split(' ')
        _M = ecdsa.ellipticcurve.Point(curve_secp256k1, int(x), int(y))
    # read the masked public key list from ./key_pairs/mask_i.txt
    masked_public_key_list = read_masked_public_key_list(10)
    # read the private key from ./key_pairs/private_key_i.txt
    private_key = read_private_key(index)
    # message is a session key
    # just a random public key here
    session_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsQZgKydNPkPVtvvqDfzCaIJVF
A1pLwQraRDOunZ6iDq2h6Xzn5AriCWCxe4tXNYvHdQp07H89ySTmZHAFQDzx79Ip
76CDTkNG1bDzNFI3TYZNtn5TyGSetHPq9QNJaEzhH4YQtNjYzfO3Ex1SptaWjX/o
UdChSVRnxJ3+LPujnQIDAQAB
-----END PUBLIC KEY-----'''
    # sign the session key via the group signature
    session_key_signature = utils.ring_signature_gen(private_key, index, session_key, masked_public_key_list, _M)
    # save signature using pickle
    with open('./signature' + str(index) + '.txt', 'wb') as f:
        pickle.dump(session_key_signature, f)