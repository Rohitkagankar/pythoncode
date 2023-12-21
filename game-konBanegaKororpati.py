questions=[["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],
["Which animal is known as the 'Ship of the Desert?","1)elephant","2)Camel","3)lion","4)horse",2],

           ]
level=[1000,2000,5000,10000,20000,50000,100000,120000,150000,300000,600000,1200000,2400000,5000000,10000000,30000000,70000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print("\n",f"{i+1}) question for {level[i]} is :")
    print(question[0],"\n",question[1],"\t",question[2],"\n",question[3],"\t",question[4])
    ans=int(input("enter the ans(1 to 4) options: "))

    if(ans==question[-1]):
        print(f"your ans is correct.")
        if(i==0):
            money=1000
            print(f"your take home money is {money} \n")
        elif(i==3):
            money=10000
            print(f"your take home money is {money} \n")
        elif(i==7):
            money=120000
            print(f"your take home money is {money} \n")
        elif(i==11):
            money=1200000
            print(f"your take home money is {money} \n")
        elif(i==13):
            money=5000000
            print(f"your take home money is {money} \n")
        elif(i==15):
            money=30000000
            print(f"your take home money is {money} \n")
        elif(i==16):
            money=70000000
            print(f"your take home money is {money} \n")
    else:
        print("wrong ans...")
        break
print("your take home money is ",money)



