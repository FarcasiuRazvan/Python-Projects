'''
Created on Jan 14, 2018

@author: Wolf
'''

def validsum(k,s,values,v):
    sum=0
    for i in range(1,k+1):
        sum=sum+values[v[i]]
    if sum==s:
        return 0
    else:
        return 1
    
def validsum1(k,s,values,v):
    sum=0
    for i in range(0,k):
        sum=sum+values[i]*v[i]
    if sum==s:
        return 1
    else:
        return 0

def iterative(coins,values,s,v):
    final=[]
    while len(v)>0:
        
        chosen=False
        while chosen==False and (len(v)<= coins) and v[-1]<1:
            v[len(v)-1]=v[len(v)-1]+1
            if len(v)<= coins:
                chosen = True
            else:
                chosen = False
        if chosen:
            if validsum1(len(v),s,values,v):
                k=[]
                for i in range(0,len(v)):
                    if v[i]==1:
                        k.append(values[i])
                if k != final:
                    afisare(values,k,len(k))
                    final=k
                v.append(-1)
            else:
                v.append(-1)
        else:
            v=v[:-1]
    if final == []:
        print("Error: the payment can't be done!")
            

def afisare(values,v,k):
    string=''
    for i in range(1,k+1):
        string=string+'a'+str(v[i])+' '
    for i in range(1,k+1):
        string=string+' '+str(values[v[i]])+' '
    print(string)
    
        
def recursive(coins,values,v,k,s):

    for i in range(v[k-1]+1,coins+1):
        v[k]=i 
        if validsum(k,s,values,v)==0:
            afisare(values,v,k)
        recursive(coins,values,v,k+1,s)

def start():
    print("How do you wnat to solve the problem ?")
    print("1. Recursive")
    print("2. Iterative")
    cmd=input("Your command: ")
    if cmd=='1':
        coins=int(input("Enter the number of coins you have: "))
        values=[]
        v=[]
        values.append(0)
        for i in range(1,coins+1):
            x=int(input("Enter the value of the coin: "))
            values.append(x)
            v.append(0)
        v.append(0)
        v.append(0)
        s=int(input("Enter the sum you want to pay: "))
        recursive(coins,values,v,1,s)
    elif cmd=='2':
        coins=int(input("Enter the number of coins you have: "))
        values=[]
        v=[]
        v.append(-1)
        for i in range(1,coins+1):
            x=int(input("Enter the value of the coin: "))
            values.append(x)    
        s=int(input("Enter the sum you want to pay: "))
        iterative(coins,values,s,v)
    else:
        print("Error: Invalid command!")


start()










if __name__ == '__main__':
    pass