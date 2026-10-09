import hashlib
import datetime

def hash_generator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class VoteBlock:
    def __init__(self, candidate_name, hash, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.candidate_name = candidate_name
        self.hash = hash
        self.previous_hash = previous_hash

    def __repr__(self):
        return (f'VoteBlock(Timestamp: {self.timestamp}, '
                f'Candidate: {self.candidate_name}, '
                f'Hash: {self.hash}, Previous Hash: {self.previous_hash})')

class VotingBlockchain:
    def __init__(self):
        initial_hash = hash_generator('initial')
        self.chain = [VoteBlock("Genesis Block", initial_hash, '0')]

    def add_vote(self, candidate_name):
        previous_hash = self.chain[-1].hash
        hash = hash_generator(candidate_name + previous_hash)
        block = VoteBlock(candidate_name, hash, previous_hash)
        self.chain.append(block)

    def verify_integrity(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != hash_generator(current.candidate_name + current.previous_hash):
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# Example usage
election = VotingBlockchain()
election.add_vote('Candidate A')
election.add_vote('Candidate B')
election.add_vote('Candidate C')

for block in election.chain:
    print(block)

# Verify the integrity of the blockchain
if election.verify_integrity():
    print("No tampering detected.")
else:
    print("Tampering detected.")

