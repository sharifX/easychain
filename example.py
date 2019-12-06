from blockchain import Message, Block, Blockchain
import pickle

B1 = Block()
B1.add_message(Message("This is the first message"))
B1.add_message(Message("Second message", "Alice", "Bob"))
B1.add_message(Message("Third message", "Bob", "Alice"))
B1.seal()

B2 = Block()
B2.add_message(Message("Fourth message"))
B2.add_message(Message("Fifth message", "Eve", "Steve"))
B2.seal()

B3 = Block()
B3.add_message(Message("Sixth message"))
B3.add_message(Message("Seventh Son of a Seventh Son is Iron Maiden's best album", "Me", "Everyone"))
B3.seal()

B4 = Block()
B4.add_message(Message("Eighth message", "Bob", "Charlie"))
B4.add_message(Message("Ninth message", "Charlie", "Daniels"))
B4.add_message(Message("Tenth message", "Charlie", "Brown"))

chain = Blockchain()
chain.add_block(B1)
chain.add_block(B2)
chain.add_block(B3)
chain.add_block(B4)

print("Validating blockchain...")
chain.validate()   # all messages and inter-message links are valid, and all blocks and inter-block links are valid

print("Serializing...")
pickle.dump(chain, open('chain.p', 'wb'))

print("Deserializing and validating...")
chain2 = pickle.load(open('chain.p', 'rb'))
chain2.validate()

print("Serializing for tampering...")
pickle.dump(chain2, open('chain.p', 'wb'))

print("Hostile tampering...")
tampered = pickle.load(open('chain.p', 'rb'))
tampered.blocks[2].messages[1].data = "Seventh Son of a Seventh Son is THE WORST ALBUM EVER MADE"  # blasphemy!
pickle.dump(tampered, open('chain.p', 'wb'))

print("Deserializing tampered chain and validating...")
chain3 = pickle.load(open('chain.p', 'rb'))
chain3.validate()       # EARTH-SHATTERING KABOOM


>>> from blockchain import Message, Block, Blockchain
>>> import pickle
>>> B1 = Block()
>>> B1.add_message(Message("Q6780787 collected S-G-3969"))
>>> B1.add_message(Message("S-G-2969 deposited at NHMUK"))
>>> B1.add_message(Message("S-G-2969 aggregated", "Q6780787", "NHMUK"))
>>> block1 = Block()
>>> B1
Block<hash: None, prev_hash: None, messages: 3, time: None>
>>> B1.__dict__
{'timestamp': None, 'messages': [Message<hash: 27b93f5bb183eea89e63ad4d98bfa13c9083d6023b034ac309e0c05e666c80a4, prev_hash: None, sender: None, receiver: None, data: Q6780787 collected S-G-39>, Message<hash: c1303ee1ce75b045380de19b61dd78d2b583f07bea580f0bff8b1cced84a48fa, prev_hash: 27b93f5bb183eea89e63ad4d98bfa13c9083d6023b034ac309e0c05e666c80a4, sender: None, receiver: None, data: S-G-2969 deposited at NHM>, Message<hash: 69d8c326efa8796360da4b28bd29367a9de96cfe1e8504660a7e7f75d3228d76, prev_hash: c1303ee1ce75b045380de19b61dd78d2b583f07bea580f0bff8b1cced84a48fa, sender: Q6780787, receiver: NHMUK, data: S-G-2969 aggregated>], 'hash': None, 'prev_hash': None}
>>> 
