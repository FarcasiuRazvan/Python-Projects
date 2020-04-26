'''
Created on Dec 18, 2017

@author: Wolf
'''

class myList():
    
    def __init__(self):
        self._list = []
        
    def __setitem__(self, position,value):
        self._list[position]= value
        
    def __getitem__(self,x):
        return self._list[x]
    
    def __delitem__(self,position):
        return self.remove(position)
    
    def __iter__(self):
        return iter(self._list)

    def append(self,e):
        self._list.append(e)
    
    def remove(self,object):
        self._list.remove(object)
        
    def pop(self,position):
        self._list.pop(position)
        
    def __len__(self):
        return len(self._list)
    
    def __str__(self,pos):
        return str(self._list[pos])    
    
def cmp(a,b):
    return a<=b

def filter(a,fct):
    x=[]
    for c in a:
        print(c)
        if fct(c)==True:
            x.append(c)
    return x

def sort(a):
    '''
    a = a vector of names/numbers
    
    GNOME SORT
    '''
    pos=0;
    while pos< len(a) :
        if pos==0 or a[pos]>=a[pos-1]:
                pos=pos+1
        else:
            aux=a[pos]
            a[pos]=a[pos-1]
            a[pos-1]=aux
            pos=pos-1
    return a

def f(x):
    return x%2==0

l = [1,2,3,4]
l1 = filter(l, f)
print(l1)