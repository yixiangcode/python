for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0 ,10):
                    if (a * 10000 + b * 1000 + c * 100 + d * 10 + e) * a == e * 111111 :
                        print(" 因为ABCDE*A=EEEEEE", "\n 所以" , "\n" , "A : " , a , "\n" , "B : ", b  , "\n" , "C : " , c ,  "\n" , "D : " , d  , "\n" , "E : " , e)
