'''
Verify the signature of the session key of consumer
'''
import utils
def verify_session_key_signature(session_key, masked_public_key_list, *session_key_signature, _M):
    # verify the signature of the session key
    return utils.verify_ring_signature(session_key, masked_public_key_list, *session_key_signature, _M)