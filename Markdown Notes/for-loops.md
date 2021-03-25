# for-loops. 

a **loop** is code that is executed over and over again.

a list of every student in a class. 

look at first student, run code
look at second student, run code

**Syntax**
> for x in **condition**:     use **in** no = or == 
    executable code

* condition is the thing you're looping through.
* executes the code in the condition.
* result is stored in **x** 
* next iteration begins. 

**range()** - function that creates a list used to loop through the code. once loop terminates the values disappear.
each value in list 

range(10) only loops through 10 times. from 0-9. the specified number is not included. 

for x in range(5)"
    print(x) 

prints 0 1 2 3 4 > 5 is not included.

x starts at 0. 
0 is in the range. 
prints 0. 
x becomes value 1
1 is in range
prints 1
x becomes 2
2 is in range.
prints 2.
The last number is not used. Stops at 4, but iterated 5 times.


for x in range(0, 5):
    print(x)
> 0 2 3 4  

begins at zero. Slices off 5. 

**you can loop through letters and strings.** 
calling a for-loop on a string 

for x in "University of Washington":
    print(x)
> University of Washington 

The range is every letter in the "string". 
Position 0 is W

for-loops only repeat a finite amount of times. you cannot have infinite loops in a for-loop

**break** - breaks your loop and stops further looping.

this requires a nested **if-statement** with a condition to break the code.

> for x in "University of Washington"
    if x == ' ':  # if there's an empty space in the string
        break     # when x is equal an empty space, stop.
   print(x)

> University    and nothing else. stops at first space.

**continue** - keep running loop but skip certain parts. 

> for x in "University of Washington"
    if x == ' ':    # if there's an empty space in the string
        continue     # when x is equal an empty space, skip.
   print(x)

> UniversityofWashington 

## while loops

while loops loop througn over and over until condition is **True**. 

> while condition:
    code execution

while loops can be infinite and crash your system. 

**You must include code that makes the while loop True so that it can terminate the loop.**

restart your kernel if in Jupyter Lab

Ctrl-C can exit out of infinite loop.
