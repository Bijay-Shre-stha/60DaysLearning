## Table of Contents

1. [Introduction to Cryptography](#introduction-to-cryptography)
2. [Caesar Cipher](#caesar-cipher)
3. [Substitution and Transposition Ciphers](#substitution-and-transposition-ciphers)
4. [Public Key Infrastructure (PKI)](#public-key-infrastructure-pki)
5. [Hashing](#hashing)
6. [Example: Caesar Cipher and Brute Force Decryption](#example-caesar-cipher-and-brute-force-decryption)
7. [Example: HTTPS and Certificates](#example-https-and-certificates)
8. [Conclusion](#conclusion)


## Cryptography: An Introduction

Cryptography involves securing communication and data through the use of codes so that only those for whom the information is intended can read and process it.

### Caesar Cipher

- One of the simplest ciphers, used over 2000 years ago.
- Shifts letters by a fixed number of places.
- Example: A shift by 3 would encrypt "A" as "D".
- Keyspace is 25, allowing 25 different keys.

### Substitution and Transposition Ciphers

- **Substitution Cipher**: Each letter is replaced by another letter.
- **Transposition Cipher**: Changes the order of the letters.
- Example: Using a key to rearrange columns and then reading the rows.

### Public Key Infrastructure (PKI)

- Ensures secure communication over HTTPS using certificates.
- Certificates signed by trusted Certificate Authorities (CAs).

## Hashing

Hash functions map data to a fixed-size array (hash value or digest). They are one-way functions that are difficult to invert and are characterized by determinism, sensitivity to input changes, and collision resistance.

### Common Hashing Algorithms

- Evolved over time; some like MD5 and SHA1 are now considered insecure.

## Example: Caesar Cipher and Brute Force Decryption

Decryption by trying all possible keys (brute force) to find the most sensible plaintext.

## Example: HTTPS and Certificates

Ensures the authenticity of websites via certificates issued by trusted authorities like DigiCert Inc.

## Conclusion

The document provides a basic understanding of cryptography, focusing on simple ciphers, public key infrastructure, and the importance of hashing. Cryptography ensures secure communication and data integrity, vital in information security.
