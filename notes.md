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

### Set

1. **Initialization**: Creating an empty set or initializing a set with values.

   ```python
   empty_set = set()
   my_set = {1, 2, 3, 4, 5}
   ```

2. **Adding Elements**: Adding an element to the set.

   ```python
   my_set.add(6)
   ```

3. **Updating with Another Set**: Adding all elements from another set to the current set.

   ```python
   my_set.update({7, 8, 9})
   ```

4. **Removing Elements**: Removing an element from the set.

   ```python
   my_set.remove(3)  # Raises an error if the element doesn't exist
   my_set.discard(4)  # Removes the element if it exists, does nothing if it doesn't
   my_set.pop()  # Removes and returns an arbitrary element
   ```

5. **Clearing**: Removing all elements from the set.

   ```python
   my_set.clear()
   ```

6. **Set Operations**: Performing various set operations, such as union, intersection, and difference.

   ```python
   union_set = set1 | set2  # Union
   intersection_set = set1 & set2  # Intersection
   difference_set = set1 - set2  # Difference
   symmetric_difference_set = set1 ^ set2  # Symmetric Difference
   ```

7. **Checking Existence**: Checking if an element exists in the set.

   ```python
   exists = value in my_set
   ```

8. **Length**: Getting the number of elements in a set.

   ```python
   length = len(my_set)
   ```

9. **Copying**: Creating a shallow copy of the set.

   ```python
   copy_set = my_set.copy()
   ```

10. **Subset and Superset**: Checking if a set is a subset or superset of another set.

   ```python
   is_subset = set1.issubset(set2)
   is_superset = set1.issuperset(set2)
   ```

11. **Disjoint Sets**: Checking if two sets have no elements in common.

   ```python
   are_disjoint = set1.isdisjoint(set2)
   ```

12. **Frozen Sets**: Creating an immutable set (frozen set).

   ```python
   frozen_set = frozenset(my_set)
   ```

13. **Set Comprehensions**: Creating a new set by applying an expression to each element of an iterable.

   ```python
   squares = {x**2 for x in my_set}
   ```

### Dictionary 

1. **Initialization**: Creating an empty dictionary or initializing a dictionary with key-value pairs.

   ```python
   empty_dict = {}
   my_dict = {"name": "Alice", "age": 30, "city": "New York"}
   ```

2. **Accessing Values**: Accessing values by key.

   ```python
   name = my_dict["name"]
   age = my_dict.get("age")  # Using the get method
   ```

3. **Adding or Updating Key-Value Pairs**: Adding a new key-value pair or updating an existing value.

   ```python
   my_dict["occupation"] = "Engineer"  # Adding a new key-value pair
   my_dict["age"] = 31  # Updating an existing value
   ```

4. **Removing Key-Value Pairs**: Removing a key-value pair by key.

   ```python
   del my_dict["city"]  # Deleting a specific key-value pair
   my_dict.pop("age")  # Removing a key-value pair using pop
   my_dict.clear()  # Removing all key-value pairs, leaving an empty dictionary
   ```

5. **Getting Keys and Values**: Getting the keys and values of a dictionary.

   ```python
   keys = my_dict.keys()
   values = my_dict.values()
   ```

6. **Iterating Over Keys and Values**: Iterating through the keys or values in a dictionary.

   ```python
   for key in my_dict:
       value = my_dict[key]
   ```

7. **Iterating Over Items**: Iterating through key-value pairs (items) in a dictionary.

   ```python
   for key, value in my_dict.items():
       # Do something with key and value
   ```

8. **Checking Existence**: Checking if a key exists in the dictionary.

   ```python
   exists = "name" in my_dict
   ```

9. **Copying**: Creating a shallow copy of the dictionary.

   ```python
   copy_dict = my_dict.copy()
   ```

10. **Dictionary Comprehensions**: Creating a new dictionary by applying an expression to each item in an iterable.

    ```python
    squared_dict = {key: value**2 for key, value in my_dict.items()}
    ```

11. **Merging Dictionaries**: Merging the contents of two dictionaries.

    ```python
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged_dict = {**dict1, **dict2}  # Python 3.5+
    ```

12. **Default Values**: Getting a value for a key with a default if the key doesn't exist.

    ```python
    value = my_dict.get("nonexistent_key", "default_value")
    ```

13. **Sorting**: Sorting the dictionary by keys or values.

    ```python
    sorted_dict = dict(sorted(my_dict.items()))
    ```

### Tuples

1. **Initialization**: Creating a tuple or initializing a tuple with values.

   ```python
   my_tuple = (1, 2, 3, 4, 5)
   ```

2. **Accessing Elements**: Accessing elements by index.

   ```python
   element = my_tuple[2]
   ```

3. **Slicing**: Creating a sub-tuple by specifying a range of indices.

   ```python
   sub_tuple = my_tuple[1:4]
   ```

4. **Length**: Getting the number of elements in a tuple.

   ```python
   length = len(my_tuple)
   ```

5. **Counting**: Counting the occurrences of a value in a tuple.

   ```python
   count = my_tuple.count(4)
   ```

6. **Finding Index**: Finding the index of the first occurrence of a value.

   ```python
   index = my_tuple.index(3)
   ```

7. **Concatenation**: Combining two or more tuples.

   ```python
   combined_tuple = tuple1 + tuple2
   ```

8. **Repetition**: Creating a new tuple by repeating the elements.

   ```python
   repeated_tuple = my_tuple * 3
   ```

9. **Checking Existence**: Checking if an element exists in the tuple.

   ```python
   exists = value in my_tuple
   ```

10. **Converting to a List**: Converting a tuple to a list.

    ```python
    my_list = list(my_tuple)
    ```

11. **Converting to a Set**: Converting a tuple to a set (removes duplicates).

    ```python
    my_set = set(my_tuple)
    ```

12. **Sorting**: Creating a sorted list from a tuple.

    ```python
    sorted_list = sorted(my_tuple)
    ```

13. **Unpacking**: Assigning multiple values to multiple variables from a tuple.

    ```python
    first, second, third = my_tuple
    ```

14. **Nested Tuples**: Creating tuples within tuples (nested tuples).

    ```python
    nested_tuple = (1, (2, 3), 4)
    ```

15. **Immutable**: Remember that tuples are immutable, so you cannot modify their elements after creation. If you need to modify a tuple, you can create a new tuple with the desired changes.
