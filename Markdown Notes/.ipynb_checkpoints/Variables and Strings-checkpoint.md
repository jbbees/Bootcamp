# Variables

**Variable** - named space in memory that is assigned a value with an equal = sign.

* declare them 
* assign a value   *variables in code need to have some kind of value.* 
* call variables 

5 common data-types to use for variables
* number 
    * integers  12
    * float  56.9
    * boolean True or False
        * They have to be written exactly as True or False, not true or false, or TRUE or FALSE
* string " "  
* list []
* dictionary {dict} - advanced list use keys to look up values. 
* tuple (tuple) - version of a list that is **unchangeable** after you assign values to them.
* nonetype - used for null values. Typed as None.

All variables need to have some value after the = sign. 

**type()** print out the data type of the variable

> var = 5.0
> print(type(var))
> <class 'float'>

Data types cannot be combined easily. Cannot have a number and a string in an expression. 

> building = 'house'
> print(building + 5)
> TypeError cannot concatenate str and int data-types.
> print(building + str(5))            *wrap the 5 part within str() function, it treats it as a string-value* 
> house5



**NOTE** Null values are accepted.

# Variable name rules

* cannot start with a number.
* cannot have spaces.
    * use an underscore_ to separate name part.
    * CapitalCase format - separate words with capital letters.
    * snakecase format - everything is lowercase and combined. 
* cannot be a reserved Python keyword.
* Names can be capitalized, but JOHN, john, and John are different.
* Can begin with an **underscore_**



you cannot 

Python natively uses **snakecase** all lower case naming 


## Format strings 

Strings are contained within " " or ' '

A **string literal** is identified as a single block of opening/closing quotes " " or ' '

Allow us to embed variables in our string print-outs, showing the value store in those variables. 

Use a lower-case f within the print() before string quotations " ".

f-strings is smart enough to take a bunch of different data types and cast them in the string. 

> money = 25.00

> print(money)
> 25.00                                         *this will print the value of the variable. It's not in a string.*

> print("I have money.")
> I have money.                                 *doesn't reference the variable. thinks it's the word money as-is in the quotes."

> print("I have {money} dollars.")
> I have ${money} dollars.                     *this prints out the variable name as presented in the quotes in the string.*

> print(f"I have ${money} dollars.)
> I have 25.00 dollars.                        *this prints the value of the embedded variable value in the string.*

{} - format activator. you put the variable in this. if not, it errors. if there is no assigned value.

###### String functions

sentence = "University of Washington"

**len()** - length of string.
> print(len(sentence))
> 24

**asterisk** - repeats strings upon print out
> print(sentence * 3)
> Univeristy of WashingtonUniversity oF WashingtonUniversity of Washington

**str()** - converts numeric data-types to a string value in the print out. useful for combining strings and numnbers
> number = 5
> print(str(5))
> 5                                    
> print(type(number))
> <class 'int'>                      *number is still an integer. the str() in print just tells interpreter to see it as string for that code. 

###### Concatenation

strings can be added together. we used the str() to combine strings and numbers.

> print("New" + "York")
> NewYork                       *no spaces*

> print(("New " + "York"))
> New York                      *put a space after new* 

> place = "New York"
> visit = "I went to "
> print(visit + place)
> I went to New York         

> place = "New York"
> visit = "I went to {}"
> print(vist.format(place))
> I went to New York                          *.format() function will embed the value of place in the {} of the visit string. 

**.format()** function - another way for formatting a string with variables. if you do not put a variable, it will error.

> beatles = "{} {} {} {}"
> print(beatles.format('john', 'paul', 'ringo', 'george'))
> john paul ringo george


Multiple string ''' or 

While strings are defined with single sets of " " or ' '    


###### Slicing strings

All strings have positions. Starting position is 0.

> school = "Univerisity of Washington"

> print(len(school))
> 24

> print(school [0])         *this will look-up 
> U                         *U is the first position of the string. Which is zero.*

> print(school [11])
> *prints nothing. a space occupies this position in the string.* 

> print(school [24])
> Error: index out of range  *even though the length of the string is 24, the beginning position is zero.*

> print(school [ ])
> ErrorL syntax           *you need to indicate a index position*

> print(school [0: 2])
> Un                       *begins at position 0, and ends at 1. It does not include position 2.* 

> print(shcool [4 : ])
> ersity of Washington     *begins at position 4 and prints rest of string.*

> print(school [ : 23])
> Univeristy of Washington    *prints everything up to position 23.*

> print(school [ : ])

**round()** function 


