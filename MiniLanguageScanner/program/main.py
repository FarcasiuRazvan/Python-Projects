'''
Created on Oct 27, 2019

@author: WOLF
'''
import re
from program.SymbolTable import *
from program.PIF import *

if __name__ == '__main__':
    pass

vect=[]
text=""
symbolsSegment0=[]
logicOperators=["AND","OR","&&","||","!=","<","<=","==",">",">="]
mathOperators=["+","-","/","*"]
ioOperators=["read","print"]
otherOperators=["<-"]
operators=mathOperators+logicOperators+otherOperators+ioOperators
codificationTable=["identifier","constant","program","int","bool","array","if","then","else","while","read","print","True","False","VAR","EXECUTE","END","AND","OR","+","-","*","/","<-","<","<=",">",">=","==","!=","&&","||","[","]","{","}",":",";"," "]

'''
 readFromFile will read the text line by line from the file date.in and do the following actions:
 - using a regex will find all the symbols, identifiers and constants including "\n" that appear in that line
 - add all the findings to a vector "vect" which is global
 - print the vector "vetc"
'''
def readFromFile():
    global vect,text
    fp = open('date.in', 'r')
    s=fp.readline()
    while s:
        p=re.compile('\w+|;|\+|-|\*|/|<-|<=|<|==|>=|>|!=|&&|\|\||\[|\]|\{|\}|:|,|\n')
        vect+=p.findall(s)
        text+=s
        s=fp.readline()
#     print(text)
    print(vect)
    fp.close()
'''
 isConstant will get as an input a string and return True if the string is a constant (boolean or integer)
 
 The function checks if it is a boolean (true/false) and return True if it is.
 Otherwise it verifies if it is a string form of digits with the first digit as a non-zero digit.
'''
def isConstant(string):
    p1=re.compile('false|true')
    if p1.findall(string)!=[]:
        if len(p1.findall(string))==1:
            return True
    p2=re.compile('[1-9]\d*')
    if p2.findall(string)!=[]:
        if p2.findall(string)[0]==string:
            return True
    return False
'''
 isIdentifier will check if a string, given as an input, is or it isn't an identifier.
 It checks if the identifier starts with a letter and then it can be composed of any letter(a-zA-Z) or digit.
'''
def isIdentifier(string):
    p1=re.compile('[a-zA-Z]\w*')
    if p1.findall(string)!=[]:
        if p1.findall(string)[0]==string:
            return True
    return False
def isExpression(i):
    expression=[]
    ok=0
    position=i
    if vect[i-1]=="print":
        expression.append("print")
    while position<len(vect):
        if vect[position] not in {";",",",":","{","}","\n","then","else","if","while"}:
            expression.append(vect[position])
        else:
            ok=1
            position=len(vect)
        position+=1
    if ok==0:
        print("Error, missing END word !!")
#     if len(expression)>1:
#         print(expression)


'''
In the function main the program will:
- call readFromFile
- initialise the PIF with the codificationTable(declared above)
- iterate through the vector and verify if the current element from the vector is identifier/constant or reserved word/symbol
- the identifier must be no more than 250 words long
- the constant must start with a non-zero digit
- if the element is an identifier/constant/symbol/reserved word the program will add it to PIF table, otherwise it will raise an error
- at the end the program will print the Symbol Table, PIF Table and the list of errors.
'''
def main():
    readFromFile()
    pif=PIF(codificationTable)
    contor=1
    segment=-1
    for i in range(0, len(vect)):
        if vect[i]=="VAR":
            segment=0
        if vect[i]=="EXECUTE":
            segment=1
        if vect[i]=="\n":
            contor+=1
        else:
            if vect[i] in codificationTable:
                if segment==0 and vect[i] in {"if","then","else","while","{","}","read","print","<-",","}:
                    print("Error at line "+str(contor)+", "+vect[i]+" not allowed in VAR section !!")  
                if segment==1 and vect[i]==":":
                    print("Error at line "+str(contor)+", : not allowed in EXECUTE section !!")  
                if segment==1 and vect[i]=="read" and not vect[i+1]==";":
                    print("Error at line "+str(contor)+", missing ; after read !!")
                if vect[i-1] in operators and vect[i] in operators:
                    print("Error at line "+str(contor)+" invalid operator "+vect[i-1]+vect[i]+" !!")
                if segment==1 and vect[i]=="print" and not(isIdentifier(vect[i+1]) or isConstant(vect[i+1])):
                    print("Error at line "+str(contor)+", can only print an identifier or a constant !!")
                if segment==1 and vect[i] in {"while","if",";","EXECUTE","{","print"}:
                    isExpression(i+1)
                pif.add_PIF(vect[i], vect[i])
            else:
                if (isIdentifier(vect[i+1]) or isConstant(vect[i+1])) and (isIdentifier(vect[i]) or isConstant(vect[i])):
                    print("Error at line "+str(contor)+" invalid identifier after identifier "+str(vect[i+1])+" "+str(vect[i])+" !!")
                    
                if isConstant(vect[i]):
                    pif.add_PIF(vect[i], "constant")
                        
                elif isIdentifier(vect[i]):
                    if len(vect[i])>250:
                        print("Error at line "+str(contor)+" identifier too long !! Identifier: "+str(vect[i]))
                    pif.add_PIF(vect[i], "identifier")
                    if segment==0 and not(vect[i+2]=="int" or vect[i+2]=="bool" or vect[i+1]=="["):
                        print("Error at line "+str(contor)+", missing : or [ after the identifier !!")
                    if segment==0:
                        symbolsSegment0.append(vect[i])
                    if segment==1 and vect[i] not in symbolsSegment0:
                        print("Error at line "+str(contor)+", identifier not declared in VAR section !!")
                    if segment==0 and vect[i+1]=="[" and isConstant(vect[i+2]) and not vect[i+3]=="]":
                        print("Error at line "+str(contor)+", missing ] !!")
                    if segment==0 and vect[i+1]=="[" and not isConstant(vect[i+2]):
                        print("Error at line "+str(contor)+", array must be declared <name>[<unsigned integer>] !!")
                else:
                    print("Error at line "+str(contor)+", symbol "+str(vect[i])+" unknown !!")
                    pif.add_PIF(vect[i],"identifier")
    
    #print(pif.to_string())
    print(pif.to_string_SymbolTable())
    print(pif.to_string())
    
    
    
    
    
    
main()
# p=re.compile('[a-zA-Z]\w*')
# print(p.findall("23d3e3e"))
# print(p.findall("23d3e3e")[0]=="23d3e3e")
#print((2+3 and 6))
# print(isConstant("true"))
# print(isConstant("false"))
    
    
    
    