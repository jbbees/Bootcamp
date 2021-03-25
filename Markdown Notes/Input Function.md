# input() function

<variable> = input(prompt or string asking for input)

the data-type of any variable entered with an input() is always a **string variable** even if you entered a number.

> age = input(38)
> print(type(variable))
> <class> 'str'>
> future_age = age + 10     *errors here.*
> print(future_age)
> Error: cannot add strings and numbers. 

in order to get age to be a number use **eval()**

**eval()** converts string to numeric. float-type
**int()** converts to integer.
**float()** converts to float.

> age = eval(input())
> age = int(input())
> age = float(input())

Let's put a prompt in the program 

prompt = '>'       *this is a string type* 

age = eval(input(prompt))

this will store the value entered into variable *prompt* as a string.
store the value of prompt into age as a number.

## Considerations

> x = input('? ')    *input a value of variable x.

Can you do this? 

> input('? ') = x      
> Error: you cannot assign to a function call.

variables are declared and named on the left of the = sign.
values are assigned to the right of = 

here python considers the variable to be input('? '), but it's an invalid name because the () makes python think it's a function. 
