from hashlib import sha256


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

MAX_NONCE = 1000000000000000000000000000000000
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yooo! Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")


if __name__=='__main__':
    transactions = '''
    Klaus->Jesse->20,
    Sandra->Laura->10
    '''

    difficulty = 5
    import time
    start = time.time()
    print("Mining...")
    new_hash = mine(5, transactions, '000000d5a11cdb44f6e482ca8620243626c761b4449784ab19c13d9ac93181ed', difficulty)
    total_time = str((time.time() - start))
    print("End Mining.")
    print(f"Mining took: {total_time} seconds")

    print(f"Mined Block is: {new_hash}")

