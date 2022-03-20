import pyperclip
import random
from data import *

tit=input("事件名称：")
keywords=input("关键词（空格分隔）：").split(" ")
print(keywords)
l=int(input("字数下限："))


def get(X):
    return X[random.randint(0,len(X)-1)]

def short(i):
    global keywords
    s=S[i]
    n=get(N)
    m=get(M)
    a=get(A)
    v=get(V)
    x=get(keywords)
    return s.replace('n',n).replace('m',m).replace('a',a).replace('v',v).replace('x',x)

def long():
    global tit
    res=get(B).replace('t',tit)+"，我"
    num=random.randint(1,5)
    num=3
    tt=random.randint(0,len(S)-1)
    for i in range(num):
        res+=short(tt)
        if i==num-1:
            res+="。"
        else:
            res+="，"
    return res

res=""
random.random()
while len(res)<l:
    res+=long()
print(res)
pyperclip.copy(res)
