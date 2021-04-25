import hashlib
from time import time
import json


class Blockchain(object):
    def __init__(self) -> None:
        self.chain = []
        self.current_trasaction = []


    def new_block(self, proof, previous_hash = None):
        # previous has is optionally none because for the genesis block
        # there is no previous block so it is not universally similar

        block = {
            'index': len(self.chain) + 1,
            'time': time(),
            'transaction':self.current_trasaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # reset the transaction history
        self.current_trasaction= []

        self.chain.append(block)
        return block


    
    def new_transaction(self, sender, recipient, amount):
        self.current_trasaction.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount,
        })

        # updates the chain index
        return self.last_block['index'] + 1

    