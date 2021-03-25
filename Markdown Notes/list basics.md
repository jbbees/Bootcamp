# Lists

* lists use []
* lists are ordered based on the order you enter the items. 
* no size limit
* heterogeneous - hold different data types.
* lists can have duplicate elements
* 0-based index. starting position is zero.
* lists have elements.


list = ['foo', 'bar', 'baz, 'qux', 'quux', 'corge']

the order each element was inserted into list is the position they have in the list.



## Finding things in a list.

You can display the list contents with or without print

> print(list)
> list            # python will just know you're referring to the list object name itself, no function.

**Find based on indexes**

look up by passing square brackets []
* only put index numbers, or number range slices, example 6:9 

print(list[index number])  print(list[5])
print(list[index number : index number]) print(list[1:7])  to find multiple items in list using a range of indexes. starting at 0.

grocery_list = ['water', 'olive oil', 'eggs', 'walnuts', 'cinnamon', 'milk']

> print(gorcery_list[:2])
> 'water', 'olive oil'                   0 - water, 1 - olive oil, 2 - eggs (omitted)

find the last 5 items on a list

> list_length = len(grocery_list)
> print(gorcery_list[(list_length-5):])
> returns 

find every other item on the list

use two colons : : in your index range  print(list[starting_index::offset]) the second number is how many its skipping.

> print(grocery_list[1::4])  gives me every 4th item in the list, starting from index 1.  

**If you want to find the index number of an item in the list 

> print(grocery_list('item')) returns the index number 

**.index()** - another built-in function for lists to display the index number of an element 

> grocery_list.index(1)                  returns the item in the 1 position. 
> variable = list.index('olive oil')     returns the numeric index where item is in list. 
1    the 1 number stored in variable.
> print(variable)
> 1
> print(grocery_list[variable])    another form of 
> [olive oil]



**Review**

print

### Changing the list adding and removing.

**.append()** - allows you to add more elements to a list. 

once you define a variable as a list-type it gains a built-in function

> list.append('john')
> list = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'john']


*NOTE: list permit duplicates* if you run index() on an element that is also duplicated in list. it will only display the first index number.

> list.append('foo')
> list = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'john', 'foo']       we have 2 values of foo in list

python reads lists from left to right, starting at position 0. 

> list.index('foo')
> 0                    it grabs the first index with the value foo.

**.remove()** - function removes elements from lists

> list.remove('foo')
> list = ['bar, 'baz', 'qux' 'quux', 'corge', 'john', 'foo']                removes the first instance of foo.

removing items in list automatically moves every other item to higher index in list. 

> list.index('bar')
> 0                       bar is now index 0. it was 1 before. 






**.pop()** - function that pops the index out of your list. 

find the index of 

find every other item on a list.

use 2 colons :

list

### Replacing items in a list

Python allows elements within a list to be changed.

you can simply just change the list outright by assigning new values.

grocery_list = ['new value', 'new value', 'new value', etc.]

the value stored in python variables can be overwritten. only the last entered value is kept. the same goes for list variables as well.

x = 1
x = 'pan'
x = 5 ** 4
x = 'house' + str(56)
x = 700

with lists you need to follow the list format [] 

**change the value of an index within a list** 

list[index number] = value      - this changes the current list element.

> grocery_list
> ['water', 'olive oil', 'eggs', 'walnuts', 'cinnamon', 'milk']

let's replace walnuts with pecans. 

find the index number

> print(grocery_list.index('walnuts')
> 3
> grocery_list[3] = 'pecans'
> grocery_list
> ['water', 'olive oil', 'eggs', 'pecans', 'cinnamon', 'milk']


