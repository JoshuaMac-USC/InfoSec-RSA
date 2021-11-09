# I don't have much experience with python (first time actually HAHAHA) so it might be a little inefficient. 
# I can't exactly get the same letters in some cases sir

p=11
q=13
e= 7
d =103
n = p*q
z=(p-1)*(q-1)



def encrypt(p,q,phrase):
    
    cipherPhrase=""
    for i in phrase:  
        m =pow(ord(i),e,n) #num,exponent,modulo
        cipherPhrase = cipherPhrase +chr(m)
    print(cipherPhrase)
    
def decrypt(p,q,phrase):
    
    normalPhrase=""
    for i in phrase: 
        c=pow(ord(i),d,n) #Same as vid but does not get same result
        normalPhrase = normalPhrase +chr(c)
    print(normalPhrase)

encrypt(p,q,"ENCRYPTION")
decrypt(p,q,"lNYECaHS(N")
encrypt(p,q,"RASTAMAN")
decrypt(p,q,"EA\HAMAN")