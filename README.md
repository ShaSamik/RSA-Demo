# RSA Encryption & Digital Signature Lab

## Overview

This project demonstrates the core concepts of RSA public-key cryptography, including key generation, encryption, decryption, digital signatures, and signature verification. The implementation is written in Python and follows a step-by-step approach to understand how RSA works internally.

---

## Features

* Generate RSA private key from given primes
* Encrypt plaintext messages using a public key
* Decrypt ciphertext using a private key
* Create digital signatures for messages
* Verify signatures for authenticity and integrity
* Demonstrate how small changes break signatures

---

## Project Structure

```
private_key.py    # Deriving private key (d)
encrypt.py        # Encrypting a message
decrypt.py        # Decrypting ciphertext
sign.py           # Signing messages
verify.py         # Verifying valid signature
corrupt.py        # Verifying corrupted signature
readme.txt        # Basic info
```

---

## How to Run

Make sure you have Python installed (Python 3 recommended).

Run each task individually:

```
python private_key.py
python encrypt.py
python decrypt.py
python sign.py
python verify.py
python corrupt.py
```

---

## Key Concepts Used

* Modular arithmetic
* Euler’s Totient Function
* Modular inverse
* Public and private key cryptography
* RSA encryption/decryption
* Digital signatures and verification

---

## Observations

* RSA encryption successfully converts plaintext into unreadable ciphertext.
* Decryption correctly restores the original message.
* Even a small change in a message produces a completely different signature.
* Corrupting a signature causes verification to fail, demonstrating integrity protection.

---

## Requirements

* Python 3.x

---

## Author

Shaharia Samik

---

## Notes

This project is to demonstrates the fundamentals of RSA cryptography without additional optimizations or security enhancements.
