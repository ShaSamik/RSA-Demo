# Signing a Message

n_hex = "2C6B161E26C58BECBCCBEFCF71A2B084017978BD13D138B990A1F070E5E213"
d_hex = "2E4012F7B247603B5115B65316201929D85AD2078006CCA57FD458E933B81"

# Convver hex to int
n = int(n_hex, 16)
d = int(d_hex, 16)

# Orignial message
original_message = "Execute the payment transaction of $5000"

# Modified message
modified_message = "Execute the payment transaction of $8000"

# Conver both messages to hex
original_message_hex = original_message.encode().hex()
modified_message_hex = modified_message.encode().hex()

# Convert hex to int
m1 = int(original_message_hex, 16) # Original message as int
m2 = int(modified_message_hex, 16) # Modified message as int

# Sign the original message
signature_original = pow(m1, d, n)

# Sign the modified message
signature_modified = pow(m2, d, n)

# Print results

print ("Original Message: ", original_message)
print ("Modified Message: ", modified_message)

print ("Original Message in hex: ", original_message_hex)
print ("Modified Message in hex: ", modified_message_hex)

print ("Signature of Original Message: ", signature_original)
print ("Signature of Modified Message: ", signature_modified)