lang=input("Enter the lang for incryption: ")

if(len(lang)<3):
    lang=lang[ : :-1]
    print(lang)
else:
    lang="srt"+lang[-1]+lang[0:-1]+"cbd"
    print(lang)

#------Anoter-------
import random
import string
st=input("enter the message: ")
words= st.split(" ")
coding=int(input("enter 1 for encoding & 0 for decoding : "))
coding=True if(coding==1) else False
print(coding)
if (coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            st1=(''.join(random.choices(string.ascii_letters, k=3)))
            st2=(''.join(random.choices(string.ascii_letters, k=3)))
            stnew=st1+word[1:]+word[0]+st2
            nwords.append(stnew)
        else:
            nwords.append(word[ : :-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if (len(word) >= 3):

            stnew = word[3:-3]
            stnew= stnew[-1]+ stnew[ : -1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))







