# pyPassGen
 a simple python random password generator with variable length of pasword

 ![main](https://user-images.githubusercontent.com/39905530/195142756-dec1550d-c216-4cf9-83ea-11b347e36663.png)
 
 # Code:
 
 ```
 import random
import multiprocessing as mp

def genpass():
    pas = ""
    txt = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    # txt = "1234567890"
    try:
        lse = int(input("Password length: "))
        for a in range(lse):
            pas += random.choice(txt)
        print(pas)
        lse = 0
    except Exception as e:
        print("Error: " + str(e))
while 1:
    genpass()
 ```
 
 
#
