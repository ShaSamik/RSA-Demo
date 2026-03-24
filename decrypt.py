# Decoding message

n_hex = "2C6B161E26C58BECBCCBEFCF71A2B084017978BD13D138B990A1F070E5E213"
d_hex = "2E4012F7B247603B5115B65316201929D85AD2078006CCA57FD458E933B81"
c_hex = "4FEC0C58B39AF2CD3F2192CD8835DA22A2B227697C98CA0DB94174B84B984"

# Convert hex to int

n = int(n_hex, 16)
d = int(d_hex, 16)
c = int(c_hex, 16)


# Decrypt
m = pow(c, d, n)

# Convert decrypted int to hex
message_hex = hex(m)[2:] # Remove 0x prefix

# Convert hex to string
message = bytes.fromhex(message_hex).decode()

# Print result

print("Ciphertext:", c_hex)
print("Decrypted hex:", message_hex.upper())
print("Plaintext message:", message)



