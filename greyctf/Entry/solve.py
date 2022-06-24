
def decrypt(m,val):
    return bytes([x ^ y for x, y in zip(m,val)])

bytes_c = bytes.fromhex("982e47b0840b47a59c334facab3376a19a1b50ac861f43bdbc2e5bb98b3375a68d3046e8de7d03b4")

key = decrypt(bytes_c[0:4],b"grey")
key = 10*key

c = b''
for i in range(0, len(bytes_c), 4):
    c += decrypt(bytes_c[i : i + 4],key)

print(c)
print(bytes.fromhex(c.hex()[2:]).decode())

#FLAg : grey{WelcomeToTheGreyCatCryptoWorld!!!!}