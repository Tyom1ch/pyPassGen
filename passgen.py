import random
import multiprocessing as mp

def genpass():
    pas = ""
    txt = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    # txt = "1234567890"
    try:
        lse = int(input("Длина паролю: "))
        for a in range(lse):
            pas += random.choice(txt)
        print(pas)
        lse = 0
    except Exception as e:
        print("Помилка: " + str(e))
while 1:
    genpass()