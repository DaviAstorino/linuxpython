import hashlib
import random

senha=input("digite sua senha: ")
print("sua senha é:",senha)
r=random.randint(0,1)
s=senha+str(r)
hash=hashlib.sha512(str(senha).encode("utf-8")).hexdigest()
print("sua senha encriptografada é:",hash)