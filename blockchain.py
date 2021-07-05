import datetime
from block import Block 

block_chain=[Block.create_genesis_block()]



print("THe genesis block has been created!")
print('Hash: %s ' % block_chain[-1].hash)


num_blocks_to_add=20

for i in range(1,num_blocks_to_add+1):

    block_chain.append(Block(block_chain[-1].hash,"Data",datetime.datetime.now()))
    print("Block #%d has been created. " % i)
    print("Block hash %s: " % block_chain[i].hash)