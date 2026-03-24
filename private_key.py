# Deriving the Private Key #

p_hex = "77E75FDC4FF067FFDC4E847C51F452F5"
q_hex = "885CED54AFFFE53E092113E62F436F0F"
e_hex = "0101"

p = int(p_hex, 16)
q = int(q_hex, 16)
e = int(e_hex, 16)

#Compute n
n = p * q

#Compute Euler's Totient Function
euler = (p - 1) * (q - 1)

# Compute d
d = pow(e, -1, euler)

# Print all
print ("n: ", n)
print ("Euler's Totient Function: ", euler)
print ("Private Key d: ", d)