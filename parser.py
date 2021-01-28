tabla = """
1 1 DatoW ACCB 9 2 0 DatoW
1 4 ACCA DatoW A 3 0 DatoW
2 4 DatoW IX B 6 0 DatoW
2 2 ACCB DatoW C 1 DatoW SP
3 4 DatoW IY C 6 ACCA DatoW
3 3 ACCB DatoW D 4 DatoW SP
4 1 DatoW 0 D 6 ACCB DatoW
5 4 DatoW 0 E 2 DatoW SP
6 1 DatoW IX E 6 IX DatoW
6 2 ACCA DatoW F 3 DatoW SP
7 1 DatoW IY F 6 IY DatoW
7 3 ACCA DatoW
8 5 DatoW 0
"""
c = 0
tabla = tabla.split("\n")[1:-1]
for r in tabla:
    r = r.split(" ")
    for d in r:
        if c == 0:
            print("IF selregW = \"{0:b}\" and".format(int(d,2)))
        elif c==1:
            print(" selregr \"{0:b}\" THEN".format(int(d)))
        elif c==2:
            print("D1 <= {};".format(d))
        else:
            print("D2 <= {};".format(d))
            c = 0
        c += 1
        
        print(d)
