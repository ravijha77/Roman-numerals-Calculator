#!/usr/bin/env python
""" The Following module does mathematical operation with Roman numerals.
    Author: Ravi Kishan Jha.
    Date: 15th November 2017.
"""
def main():
    
    '''This Function is the main function of the code. performs Arithmetic operations on the Roman
    Numbers
    Input Attributes: Roman Value1 of String type, Roman Value 2 of String Type
    The Code has the use of operater on input attributes to perform different arithmetic operations
    Output Attribute: Roman Value of Arithmetic operation of input String values. '''
    
    num1 = input().upper()
    op = input()
    num2 = input().upper()
    if (check_correct_roman(num1) == 1 and check_correct_roman(num2) == 1):
        if (op == '+'):
            result = add(num1,num2)
        elif (op == '-'):
            result = sub(num1,num2)
        elif (op == '/'):
            result = div(num1,num2)
        elif (op == '*'):
            result = mult(num1,num2)
        print(result)
    else:
        print("error")

def check_correct_roman(s):
    
    ''' This function is used to check whether the INPUT Roman Number is valid or not.
    Input attribute : Type String, is a roman number with letters such as C, X, L, V, I, M
    Output is either 1 or 0 based on the condition satisfied.'''
    
    if(len(s) < 4):
        return 1
    for pos in range(0, len(s)-3):
        if(s[pos] == s[pos + 1] == s[pos + 2] == s[pos + 3]):
            return 0
        else:
            return 1

def integer_to_roman(num):
    
    ''' This function is used to convert the integer value into its respective Roman value.
    Input Attribute: Integer Value from range 1 to 3999 usually
    Output Attribute : Roman Number which is string value of the corresponding Integer.'''
    
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
     (100, 'C'), (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), 
     (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    if(num < 4000):
        roman = ''
        while num > 0 :
            for temp, roman_temp in num_map:
                while num >= temp:
                    roman += roman_temp
                    num -= temp
        return roman
    else:
        print("Out of range")

def roman_to_integer(s):
    
    '''This Function is converting the Roman number into it's respective integer value.
    Input Attribute: String Roman Value usually containing values such as C, M, X, V, I, D.
    Output Attribute: Integer Value of the corresponding input Roman string.'''
    
    roman_map = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    temp = 0
    for i in range(0, len(s)-1):
        if roman_map[s[i]] < roman_map[s[i + 1]]:
            temp -= roman_map[s[i]]
        else:
            temp += roman_map[s[i]]
    return temp + roman_map[s[-1]]

def add(num1, num2):
    
    '''This Function performs Arithmetic operations on the Roman Numbers.
    Input Attributes: Roman Value1 of String type, Roman Value 2
    of String Type
    The Code has conversion of input attributes using external functions Roman to Integer, perform 
    operations and then convert Integer to Roman.
    Output Attribute: Roman Value of Addition of input String values.'''
    
    val1 = roman_to_integer(num1)
    val2 = roman_to_integer(num2)
    return integer_to_roman(val1 + val2)

def sub(num1, num2):
    
    '''This Function performs Arithmetic Subtraction on the Roman Numbers.
    Input Attributes: Roman Value1 of String type, Roman Value 2
    of String Type
    The Code has conversion of input attributes using external functions Roman to Integer, perform 
    operations and then convert Integer to Roman.
    Output Attribute: Roman Value of Subtraction of input String values.'''
    
    val1 = roman_to_integer(num1)
    val2 = roman_to_integer(num2)
    if (val1 > val2):
        return integer_to_roman(val1 - val2)
    else:
        return integer_to_roman(val2-val1)

def mult(num1, num2):
    '''This Function performs Multiplication operation on the Roman Numbers.
    Input Attributes: Roman Value1 of String type, Roman Value 2
    of String Type
    The Code has conversion of input attributes using external functions Roman to Integer, perform 
    operations and then convert Integer to Roman.
    Output Attribute: Roman Value of Multiplication of input String values.'''
    
    val1 = roman_to_integer(num1)
    val2 = roman_to_integer(num2)
    return integer_to_roman(val1 * val2)

def div(num1, num2):
    '''This Function performs Division operation on the Roman Numbers.
    Input Attributes: Roman Value1 of String type, Roman Value 2
    of String Type
    The Code has conversion of input attributes using external functions Roman to Integer, perform 
    operations and then convert Integer to Roman.
    Output Attribute: Roman Value of Division of input String values.'''

    val1 = roman_to_integer(num1)
    val2 = roman_to_integer(num2)
    return integer_to_roman(val1 / val2)


if __name__ == '__main__':
    main()
