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
## String concatenation
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
## User input
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
## Formatting floating-point numbers
```
>>> format(10.123456789, "10.2f")
'     10.12'
>>> format(10.123456789, "1.2f")
'10.12'
>>> format(10.123456789, ".2f")
'10.12'
>>> format(10.123456789, ".5f")
'10.12346'
``` 

## Formatting in Scientific Notation
```
>>> format(99.123456, "10.2e")
'  9.91e+01'
>>> format(99.123456, "5.2e")
'9.91e+01'
>>> format(99.123456, ".2e")
'9.91e+01'
>>> format(99.123456, ".4e")
'9.9123e+01'
```

## Formatting as Percentage
```
>>> format(0.5, ".4%")
'50.0000%'
>>> format(0.5, "1.2%")
'50.00%'
>>> format(0.5, "10.2%")
'    50.00%'
>>> format(0.456, "10.2%")
'    45.60%'
>>> format(.455, ".2%")
'45.50%'
``` 
## Collection data types

### List

1. **Initialization**: Creating an empty list or initializing a list with values.

   ```python
   empty_list = []
   values_list = [1, 2, 3, 4, 5]
   ```

2. **Appending**: Adding an element to the end of the list.

   ```python
   my_list.append(6)
   ```

3. **Extending**: Extending a list by appending elements from another iterable.

   ```python
   my_list.extend([7, 8, 9])
   ```

4. **Inserting**: Inserting an element at a specific index.

   ```python
   my_list.insert(2, 'new_value')
   ```

5. **Removing**: Removing the first occurrence of a value from the list.

   ```python
   my_list.remove(3)
   ```

6. **Popping**: Removing and returning an element from a specific index.

   ```python
   popped_value = my_list.pop(1)
   ```

7. **Indexing**: Accessing elements by their index.

   ```python
   value = my_list[2]
   ```

8. **Slicing**: Creating a sub-list by specifying a range of indices.

   ```python
   sub_list = my_list[1:4]
   ```

9. **Length**: Getting the number of elements in a list.

   ```python
   length = len(my_list)
   ```

10. **Counting**: Counting the occurrences of a value in a list.

    ```python
    count = my_list.count(4)
    ```

11. **Sorting**: Sorting the list in ascending or descending order.

    ```python
    my_list.sort()
    my_list.sort(reverse=True)
    ```

12. **Reversing**: Reversing the order of elements in the list.

    ```python
    my_list.reverse()
    ```

13. **Copying**: Creating a shallow copy of the list.

    ```python
    copy_list = my_list.copy()
    ```

14. **Clearing**: Removing all elements from the list.

    ```python
    my_list.clear()
    ```

15. **Checking Existence**: Checking if a value exists in the list.

    ```python
    exists = value in my_list
    ```

16. **Concatenating**: Combining two or more lists.

    ```python
    combined_list = list1 + list2
    ```

17. **List Comprehensions**: Creating new lists by applying an expression to each element of an existing list.

    ```python
    squares = [x**2 for x in my_list]
    ```

18. **Filtering with List Comprehensions**: Creating a new list by filtering elements based on a condition.

    ```python
    even_numbers = [x for x in my_list if x % 2 == 0]
    ```

19. **Mapping with List Comprehensions**: Creating a new list by applying a function to each element.

    ```python
    doubled_values = [x * 2 for x in my_list]
    ```

20. **List unpacking**: Assigning multiple values to multiple variables from a list.

    ```python
    first, second, third = my_list
    ```

These are some of the most commonly used functions and operations with Python lists. You can use them to manipulate and work with lists in your Python programs.




