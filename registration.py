"""
Registration is responsible for the registration of new users' key pairs.
"""

from utils import key_gen

# generate 10 new key pairs
# as 10 users

private_key, public_key = key_gen(10)

# save the private key and public key to 10 files
# each file contains the private key and the public key of one user
# path: e.g. ./key_pairs/private_key_0.txt
for i in range(10):
    with open('./key_pairs/private_key_' + str(i) + '.txt', 'w') as f:
        f.write(str(private_key[i]))
    with open('./key_pairs/public_key_' + str(i) + '.txt', 'w') as f:
        f.write(str(public_key[i]).replace('(', '').replace(')', '').replace(',', ' '))