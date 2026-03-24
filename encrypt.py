# Encrypting Message

#given data
message = "Encrypting data!"
n_hex = "2C6B161E26C58BECBCCBEFCF71A2B084017978BD13D138B990A1F070E5E213"
e_hex = "10001"
d_hex = "2E4012F7B247603B5115B65316201929D85AD2078006CCA57FD458E933B81"

# Convert hex to int
n = int(n_hex, 16)
e = int(e_hex, 16)

#Converting message to hex
message_hex = message.encode().hex()
m = int(message_hex, 16)

# Encrypyt
c = pow(m, e, n)

# Print result
print("Message: ", message)
print("Message in hex: ", message_hex)
print("Ciphertext: ", hex(c))
