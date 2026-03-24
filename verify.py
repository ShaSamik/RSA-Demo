# Verifying signature

message = "Execute transaction."
s_hex = "5F8383D23E041F97277CEB35DE83ED6B291B78791D399B759DD98498FE3"
e_hex = "10001"
n_hex = "6186ED97833F051F91E36FD337AF65399B32E8C56ECF5DEC89CC97B9FAF"

# Convert hex to int
m_hex = message.encode().hex()
m = int(m_hex, 16)
s = int(s_hex, 16)
e = int(e_hex, 16)
n = int(n_hex, 16)

# Verify signature
verification = pow(s, e, n)

# Convert verification result to hex
recovered_hex = hex(verification)[2:]

# Add leading zero if needed
if len(recovered_hex) % 2 != 0:
    recovered_hex = "0" + recovered_hex

# Convert hex to string

recovered_message = bytes.fromhex(recovered_hex).decode()
verification_result = verification == m # True or False

# Print results
print("Original message:", message)
print("Original message hex:", m_hex.upper())
print()
print("Recovered message:", recovered_message)
print("Recovered message hex:", recovered_hex.upper())
print()
print("Signature valid?", verification_result)



