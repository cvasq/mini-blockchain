import date as date

def create_genesis_block():
    # Manually construct a block
    # index zero and arbitrary previous hash

    return Block(0, date.datetime.now(), "Genesis Block", "0")
