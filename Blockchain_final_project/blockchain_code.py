# Used the code from IBM Blockchain (Create blockchain app from Scratch)
# Most of it is same, but the some of the code/pseudocode is written from the project specification

from hashlib import sha256
import json
import time


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    # This is the difficulty for the proof of work algorithm
    difficulty = 2

    def __init__(self):
        self.chain = []

    def genesis_block(self):
        gen_block = Block(0, [], 0, "0")
        gen_block.hash = gen_block.compute_hash()
        self.chain += [gen_block]

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False
        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    # Above code is from the IBM website, I haven't added all the functions, just a few of them
    # Below I have written some function to be added to the ERP we are trying to create

    def expense_tracker(self):
        expense_employee = 0
        total_payroll = 0
        revenue_generated = 0
        # Can add an if statemet related to the revenuw generated and how to maximize it

    def data_info(self):
        # customer_info()
        # Could be a function called here, where customer information is stored and displayed
        # when the user logs in to the Blockchain ERP website
        production = 0
        # Production information, how much traffic is generated and so on
        # statistics()
        # Gathers all the information and calculates all the statistics related information
        # Allows to improve the business model for the customers and to attract more customers

    # Just a small snippet of how this function can be used
    def statistics(self):
        # The values decide what the rating of the customer is from a business POV
        customer = [1, 2, 5, 7, 12, 18]
        benefit = 0

        for i in customer:
            # If the rating of the customer is greater than 6
            # Maybe it takes at least 2 years for an average customer to reach this rating
            if customer[i] > 6:
                # Some code that the customer is entitled to more benefits
                benefit = 1
                print(customer)
        return benefit

    # The customer basic information like bank account details, personal information and all those function are
    # obvious so I didn't write a function regarding that here. Instead I tried something different with the
    # statistics function above
