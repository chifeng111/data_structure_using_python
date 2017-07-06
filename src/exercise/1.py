# coding: utf-8
from basicDataStructure.mystack import Stack

def baseConverter(decNumber,base):
    '''将一个数（十进制数）转化为任意进制
    '''
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)  #将余数放入栈中
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter.__doc__)
print(baseConverter(25,2))
print(baseConverter(25,16))