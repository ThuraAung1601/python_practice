# Notes taken from Computer Programming class

## Data types
- Python has int, float, char, str and bool literal data types.
- Use type() to check data types.
```
python
>>> type(8.7e-4)
<class 'float'>
>>> type(0xfa)
<class 'int'>
>>> type(True)
<class 'bool'>
```
## Variable
```
x = 1
print(x) # 1
```
# Arithmetic operations
```
>>> 5+10
15
>>> 9-8
1
>>> 9*8
72
>>> 9/3
3.0
>>> 9//3
3
>>> 8%3
2
>>> 8/3
2.6666666666666665
```

```
+=   Addition assignment          i += 8 
-=   Subtraction assignment       i -= 8
*=   Multiplication assignment    i *= 8 
/=   Float division assignment    i /= 8 
//=  Integer division assignment  i //= 8 
%=   Remainder assignment i %= 8  i = i % 8
**=  Exponent assignment i **= 8  i = i ** 8
```

## Basic mathematical operations
```
>>> var_x = 3.1428
>>> var_y = int(var_x)
>>> var_y
3
>>> var_x
3.1428
>>> round(var_x,2)
3.14
>>> var_x
3.1428
 
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sin(2*math.pi)
-2.4492935982947064e-16
>>> math.pi
3.141592653589793
>>> math.cos(2*math.pi)
1.0
>>> min(2,2,1,9,6)
1
>>> max(2,2,1,9,6)
9
>>> abs(-4.4443)
4.4443
>>> math.ceil(-2.5)
-2
>>> math.floor(-2.5)
-3
>>> math.ceil(2.5)
3
>>> math.floor(2.5)
2
>>> round(3.5)
4
>>> round(3.55555,2)
3.56
>>> round(-2.4)
-2
>>> round(-2.6)
-3
>>> math.fabs(2.5)
2.5
>>> math.fabs(-2.5)
2.5
``` 
## Strings and characters
```
>>> num = 3
>>> num >= 0x30 and num <= 0x39
False
>>> ord(num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected string of length 1, but int found
>>> ord(str(num))
51
>>> num = ord(str(num))
>>> num >= 0x30 and num <= 0x39
True
```
- String concatenation
```
>>> message1 = "Welcome to" + "KMITL."
>>> message2 = "I am Thura. \n She is Ei."
>>> message = message1 + message2
>>> message1
'Welcome toKMITL.'
>>> message2
'I am Thura. \n She is Ei.'
>>> message 
'Welcome toKMITL.I am Thura. \n She is Ei.'
```
- In Python, user input is string data types.
```
>>> val = input("Enter ur name: ")
Enter ur name: Thura
>>> val
'Thura'
>>> val = input("Enter ur age: ")
Enter ur age: 21
>>> val
'21'
>>> type(val)
<class 'str'>
>>> val = eval(input("Enter ur age:"))
Enter ur age:21
>>> val
21
>>> type(val)
<class 'int'>
``` 




