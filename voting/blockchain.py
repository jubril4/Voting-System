# voting/blockchain.py

import hashlib
import datetime

def hash_generator(data):
    return hashlib.sha256(data.encode()).hexdigest()

class VoteBlock:
    def __init__(self, candidate_name, hash, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.candidate_name = candidate_name
        self.hash = hash
        self.previous_hash = previous_hash

    def __str__(self):
        return (f'[{self.timestamp}] - Vote for {self.candidate_name} '
                f'(Hash: {self.hash}, Previous: {self.previous_hash})')

class VotingBlockchain:
    def __init__(self):
        initial_hash = hash_generator('initial')
        self.chain = [VoteBlock("Genesis", initial_hash, '0')]

    def add_vote(self, candidate_name):
        previous_hash = self.chain[-1].hash
        hash = hash_generator(candidate_name + previous_hash)
        self.chain.append(VoteBlock(candidate_name, hash, previous_hash))

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != hash_generator(current_block.candidate_name + current_block.previous_hash):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

