"""
Trust Anchor (TA)
Responsible for:
    - Generating the mask
    - Generating the masked public key
    - Generating the masked public key list
"""
import ecdsa
from ecdsa.ecdsa import curve_secp256k1
from ecdsa.util import randrange
from ecdsa.curves import SECP256k1

# Read the unmasked public key list from ./key_pairs/public_key_i.txt
# the public key is stored in the form of two strings split by a space
# convert the two strings to Point object
def read_public_key_list(number_participants):
    public_key_list = []
    for i in range(number_participants):
        with open('./key_pairs/public_key_' + str(i) + '.txt', 'r') as f:
            x, y = f.read().split(' ')
            public_key_list.append(ecdsa.ellipticcurve.Point(curve_secp256k1, int(x), int(y)))
    return public_key_list

# generate a random mask
def generate_mask():
    mask = randrange(SECP256k1.order)
    return mask

# generate the masked public key
def generate_masked_public_key(public_key, mask):
    masked_public_key = public_key * mask
    return masked_public_key

# generate the masked public key list
def generate_masked_public_key_list(public_key_list, mask):
    masked_public_key_list = list(map(lambda yi: yi * mask, public_key_list))
    return masked_public_key_list

if __name__ == '__main__':
    public_key_list = read_public_key_list(10)
    mask = generate_mask()
    _M = generate_masked_public_key(SECP256k1.generator, mask)
    masked_public_key_list = generate_masked_public_key_list(public_key_list, mask)
    # save the mask and masked public key list to 10 files
    # each file contains the masked public key list of one user
    # path: e.g. ./key_pairs/mask_0.txt
    for i in range(10):
        with open('./key_pairs/mask_' + str(i) + '.txt', 'w') as f:
            f.write(str(masked_public_key_list[i]).replace('(', '').replace(')', '').replace(',', ' '))

    # save _M to ./key_pairs/mask_M.txt
    with open('./key_pairs/mask_M.txt', 'w') as f:
        f.write(str(_M).replace('(', '').replace(')', '').replace(',', ' '))