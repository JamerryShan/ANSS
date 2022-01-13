# ANSS Course

This is a demo for the ANSS Course. 

It is heavily based on the vehicle sharing system [HERMES: Scalable, Secure, and Privacy-Enhancing Vehicular Sharing-Access System
](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9477257) and the group signature scheme [Linkable Spontaneous Anonymous Group Signature for Ad Hoc Groups](https://eprint.iacr.org/2004/027.pdf).

In the original HERMES system, the session keys are forwarded by the vehicle owners to the service providers, which means that the session keys might be chenged to a fake one by vehicle owners. So, the group signature scheme is used to ensure that the session keys are not changed when it reaches the service providers. Besides, a trusted authority is introduced to mantain the public key list, and TA will mask the public key list to make sure that even if the VSSP knows the public key list, it cannot tell which user is in which group. (Try to reach the group signature based zero-knowledge proof.)

### Stuff used in this demo
 * [ECDSA](https://github.com/warner/python-ecdsa) ECDSA cryptography python library. 
 * The group signature scheme is implemented based on the [implementation](https://github.com/fernandolobato/ecc_linkable_ring_signatures) of Linkable Spontaneous Anonymous Group Signature for Ad Hoc Groups.

### Structure of the demo
This demo consists of the following parts:
* Trusted Authority -- The trusted authority is a central authority that is trusted by all the participants. It is responsible for the management of the group and public keys list distribution.
* Consumer -- The consumer is a participant that wants to join the group. It is responsible for generation of signature of the session keys which is used to make sure the session key is valid and unchanged when it reaches the VSSP.
* VSSP(Vehicle Sharing Service Provider) -- The VSSP is responsible for verifying the signature of the group signature is valid and is signed by the trusted consumer.

### How to run the demo
First, the consumer needs to run the registration.py script, to register itself to the trusted authority. It will generate a private key and a public key, which will be sent to the trusted authority. The generated keys will be stored in the consumer's local directory.
```
python registration.py
```
Then, the trusted authority will generate a secure random group key and a public key as a mask for the consumer's public key. The consumer's public key will be masked by the private key of the trusted authority. The masked public key list will be public.
```
python TA.py
```
The consumer will run the consumer.py script, which will generate a signature of the session key. The consumer will send the signature to the VSSP. The VSSP will verify the signature and the session key is valid and unchanged by using the masked public key list.
```
python consumer.py
```
The VSSP will run the VSSP.py script, which will verify the signature of the group signature.
```
python VSSP.py
```