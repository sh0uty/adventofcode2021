"""
Packet is in hexadecimal
First convert to binary
Bit 0-2 = Packet Version
Bit 3-5 = Packet Type (ID)

Packet Type (ID)
4 = literal value
Literal values encode a single binary number
Padded with zeros in the front to be a multiple of 4
Then split in 4-bit chunks with a 1 prefix for each chunk but last chunk has a 0 prefix
Example: D2FE28 becomes 110100101111111000101000 = VVVTTTAAAAABBBBBCCCCC

Next interpret the binary string as follows:
First three bits are the packet version ex: 110=6 is represented by VVV
Next three bits are the packet type ex: 100=4 is represented by TTT
Next five bits here AAAAA = 10111 = remove the first one because not last chunk = 0111
Next five bits here BBBBB = 11110 = remove the first one because not last chunk = 1110
Next five bits here CCCCC = 00101 = remove the first one because not last chunk = 0101
Last three zeros are ignored because of hexadecimal padding
Thus the literal value in the packet is 011111100101 = 2021 in decimal
"""

with open('test_input', 'r') as f:
    data = f.readline()

stream_len = len(data)*4
stream = (bin(int(data, 16))[2:]).zfill(stream_len)
print(f'{stream=}')

def decode_type4_packet(stream):
    unformatted = []
    zero = False
    factor = 0
    while not zero:
        tmp = stream[6+5*factor:11+5*factor]
        print(f'{chr(factor + 65)} = {tmp}')
        unformatted.append(str(tmp))
        if tmp[0] == '0':
            zero = True
        factor += 1
    print(f'{unformatted=}')
    num = int(''.join([i[1:5] for i in unformatted]), 2)
    print(f'{num=}')
    padding = factor*5 % 4
    return 6 + 5*factor + padding

while stream:
    version = stream[0:3]
    type_id = stream[3:6]

    if type_id == '100':
        print(f'{version=}')
        end_of_packet = decode_type4_packet(stream)
        stream = stream[end_of_packet:]
    else:
        print(f'{version=}')
        length_type_id = stream[6]
        if length_type_id == '0':
            length_of_packets = int(stream[7:22], 2)
            stream = stream[22:]
            sub_stream = stream[:length_of_pgackets]
            current_length = 0
            print(f'{length_of_packets=}')
            while True:
                if current_length >= length_of_packets:
                    break
                print(f'{sub_stream=}')
                end = decode_type4_packet(sub_stream) - 1
                print(f'{end=}')
                current_length += end # ! Wrong length is getting calculated
                sub_stream = sub_stream[end:]
                print(f'{current_length=}')
            stream = stream[length_of_packets:] # ! Somehow wrong padding because of eg: padding is 0000000 why not only 3 000 to get a multiple of 4????
                
                

