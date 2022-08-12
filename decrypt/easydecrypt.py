import string
import sys
#from secret import MSG
alphabet = string.ascii_letters+string.digits + "_@{}-/()!\"$%=^[]:;"

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * ord(char) + 18) % 256)
    return bytes(ct)

def decrypt():
    with open('./msg.enc','rb') as f:
        byte = f.read(2)
        while byte:
            intInFile = int(byte,16)
            for char in alphabet:
                encodedChar = ((123 * ord(char) + 18) % 256)
                if encodedChar == intInFile:
                    print(char)

            byte = f.read(2)

    # with open('./msg.enc','rb') as f:
    #     byte = f.read(2)
    #     while byte:
    #         decByte = int.from_bytes(byte, byteorder=sys.byteorder)
    #         #print(decByte)
    #         for char in alphabet:
    #             encodedChar = ((123 * ord(char) + 18) % 256)
    #             if encodedChar == decByte:
    #                 print(char)
    #
    #         byte = f.read(2)
    #
    #     f.close()
    #
    #

decrypt()
print(int.from_bytes(encryption("X"), byteorder=sys.byteorder))
#ct = encryption("Mesa")
#f = open('./msg.enc','w')
#f.write(ct.hex())
#f.close()

