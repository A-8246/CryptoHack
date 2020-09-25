from Crypto.PublicKey import RSA

f = open('p.pem','r')
key = RSA.importKey(f.read())

print(key.d)


'''
 RSAPrivateKey ::= SEQUENCE {
     version Version,
     modulus INTEGER, -- n
     publicExponent INTEGER, -- e
     privateExponent INTEGER, -- d                                    # we want this
     prime1 INTEGER, -- p
     prime2 INTEGER, -- q
     exponent1 INTEGER, -- d mod (p-1)
     exponent2 INTEGER, -- d mod (q-1)
     coefficient INTEGER -- (inverse of q) mod p }
     
You can read this value manually upload your PEM file to <https://lapo.it/asn1js/> and hit
decode and read fourth value according to the structure given above.
'''
