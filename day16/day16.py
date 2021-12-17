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

stream = list(''.join(bin(int(b, 16))[2:].zfill(4) for b in data.strip()))

def to_int(x, y = 10):
    return int(''.join(x),y)

def parse_packet(packet):
    version = to_int(packet[:3], 2)
    packet[:] = packet[3:]

    typeid = to_int(packet[:3], 2)
    packet[:] = packet[3:]

    if typeid == 4:
        number = []
        while True:
            prefix = packet.pop(0)
            number += packet[:4]
            packet[:] = packet[4:]
            if prefix == '0':
                return version, typeid, to_int(number, 2)
    else:
        packets = []
        length_type_id = packet.pop(0)
        if length_type_id == '0':
            length = to_int(packet[:15], 2)
            packet[:] = packet[15:]
            sub_packet = packet[:length]
            packet[:] = packet[length:]
            while sub_packet:
                packets.append(parse_packet(sub_packet))
        else:
            number_of_sub_packets = to_int(packet[:11], 2)
            packet[:] = packet[11:]
            for _ in range(number_of_sub_packets):
                packets.append(parse_packet(packet))
        return version, typeid, packets

def versionsum(packets):
    version = packets[0]
    if packets[1] == 4:
        return version
    else:
        return version + sum(versionsum(packet) for packet in packets[2])

print(versionsum(parse_packet(stream)))