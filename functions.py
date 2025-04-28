def ArithmitikiProodos():
        print("Give me the first serum of the sequence")
        a1 = int(input())
        print("Give me the difference of serum")
        w = int(input())
        print("Give me a natural number")
        n = int(input())  
        an = a1 + (n - 1) * w
        print("The ",n," number is " , an)

def ArthrismaArithmitikisProodou():
        print("Give me the first serum of the sequence")
        a1 = int(input())
        print("Give me the difference of serum")
        w = int(input())
        print("Give me a natural number")
        n = int(input())  
        Sn = n/2 * ( 2 * a1 *(n-1) * w )
        print("The sum of the sequence is" , Sn)

def GeometrikiProodos():
        print("Give me the first term of the geometric sequence")
        a1 = int(input())
        print("Give me the common ratio")
        r = int(input())
        print("Give me a natural number")
        n = int(input())  
        an = a1 * r ** (n-1)
        print("The ",n," number is " , an)

def ArthrismaGeometrikisProodou():
        print("Give me the first term of the geometric sequence")
        a1 = int(input())
        print("Give me the common ratio")
        r = int(input())
        print("Give me a natural number")
        n = int(input())
        Sn = (r ** n - 1) / (r - 1)
        print("The sum of the sequence is", Sn)
