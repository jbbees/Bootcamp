# Dictionaries

* unordered
* hetereogenous, holds different data-types
* collection of key-value pairs 
* keys have to be unqiue. 


lookup value is the **key** and each key MUST be unqiue.

use {} not []

dictionary_name = {'key': 'value', 'key': 'value', 'key': 'value', 'key': 'value'}

## Looking up things in dictionaries

Remember with lists you first had to know the index that item was in. passing []

print(list_name[index number])  returns the item/value stored in that position. or in range print(list_name[index # : index #])

or the .index() function

list.index(index number)

You want to look-up an item: print(list_name('item')   returns the index number/position 


within dictionaries 

### For-Loops

when we loop through a list, it returns the element stored in the index.
when we loop through a dictionary, it returns the key value, but not the item or element/value stored for that key. 

for key in trading_pnl:
    print(key)
    
  
#### BUILT-IN FUNCTIONS with dicitionaries.   
  
is this string in this dictionary?


.items() function. 

for key, value in dictionary.items():            

