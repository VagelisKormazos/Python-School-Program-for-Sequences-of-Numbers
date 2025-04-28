import functions
choice=1
while choice != 0:
    print("In this program you can calculate\n",
    "0.Press 0 if you want to exit\n",
    "1.The N term of an arithmetic sequence\n",
    "2.The sum of the n terms of an arithmetic sequence\n",
    "3.The N term of a geometric sequence\n",
    "4.The sum of the n terms of a geometric sequence\n")
    print("What's your choice?")
    choice = int(input())
    #exit
    if (choice == 0):
        break
    #niostos arithmitiki proodos
    if (choice == 1):
        functions.ArithmitikiProodos()
    #arthrisma arithmitikis
    elif(choice == 2):
        functions.ArthrismaArithmitikisProodou()
    #niostos ths Geometrikis proodou
    elif (choice == 3):
        functions.GeometrikiProodos()
    # arthrisma ths Geometrikis proodou
    elif (choice == 4):
        functions.ArthrismaGeometrikisProodou()
    #wrong choice
    else:
        print("wrong choice")

    print("_____________________________________________________________________")

