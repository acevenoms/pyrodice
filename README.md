pyrodice
========

An interactive command-line dice roller written in python that can take advantage of advanced random number generators

Method
------

Interactive shell style interface. Interaction is through instructional verbs, like an assembly language.
Example:

```
[roll]>> 3d10
[9, 1, 8]
[3d10+0]>> sum
18
[3d10+0]>> bye
```

The first instruction (in the form of standard RPG dice rolling notation) is to roll a Set of dice
The result is a list of random numbers
The second instruction is to sum the rolls
The result is the sum

Plans for the future could see this turn into a Lisp-like language

Planned/Conceptual verbiage
---------------------------

Standard RPG dice rolling syntax, parsed by this regex: (\d*)d(\d+)([+-]\d+)?
Example:

```
>> 3d10+7
[15, 9, 11]
```

***

Display strings, litteral printed messages
Example:

```
>> "Hello, pyrodice!"
Hello, pyrodice!
```

***

```
sum [expr]
```

***
Sums the a result if it is a list (pretty much a direct mapping to the python sum() built-in)
Examples:
>> 3d10
[9, 1, 8]
>> sum
18

>> sum 4d6
12

reroll [above|below] <val> [expr]
Replaces all instances of val in the given results list with a new roll of the same die. 
If above/below is specified, all results above or below val are rerolled, non-inclusive.
This is not recursive, if the new roll matches the reroll rule, it will not be rerolled again.
Example:
>> 10d20
[5, 9, 16, 4, 17, 1, 12, 17, 11, 7]
>> reroll 17
[5, 9, 16, 4, 18, 1, 12, 3, 11, 7]
>> reroll above 10
[5, 9, 5, 4, 11, 1, 3, 4, 5, 7]
>> reroll below 5
[5, 9, 5, 7, 11, 19, 8, 12, 5, 7]

count [above|below] <val> [expr]
Counts the instances of val in the given results.
If above/below is specified, all results above or below val are counted, non-inclusive.
Examples:
>> 12d6
[4, 6, 1, 4, 3, 1, 3, 4, 5, 6, 1, 1]
>> count 1
4

>> 12d6
[4, 1, 4, 2, 2, 5, 1, 4, 2, 5, 4, 3]
>> count above 4
2

>>count below 5 12d6
10

append <expr> [expr]
Appends two results into a single result list
Examples:
>> 5d2
[1, 2, 2, 2, 1]
>> append 2d100
[1, 2, 2, 2, 1, 29, 74]

>> 3d8
[7, 1, 5]
>> append sum
[7, 1, 5, 13]

define [[space...].]<name> <expr...>
Defines and names a dice rolling procedure. Multiple expressions can be delineated with the semicolon.
These definitions are persistent between restarts, they are added to the default environment as special verbs that may be called by adding a leading dot (.)
They can also be contained in namespaces, to avoid really ugly names with underscores and so on.
Procedures that are single expressions will be evaluated as is and display their result as they normally would.
Procedures with multiple expressions will not display the results of individual expressions unless explicitly told to with the display verb.
The display verb evalutes exactly as the expression it displays would (e.g. display 2d10 gives the same result as 2d10) 
Examples:
>> define longsword sum append 2d10+3 1d6
.longsword defined
>> .longsword
16

>> define new.longsword "Physical: "; display 2d10+3; " = "; sum; "\nFire: "; display 1d6; " = "; sum;
.new.longsword defined
>> .new.longsword
Physical: [8, 13] = 21
Fire: [6] = 6

save [persist] [[space...].]<name> [expr]
Saves a result in a named variable. These only persist between restarts if they are explicitly told to.
Variables can be recalled by putting a dollar sign in front of them. Like procedures, they can be contained in namespaces.
Examples:
>> save greataxe 2d12
Saved [3, 8] as $greataxe
>> $greataxe
[3, 8]
>> sum $greataxe
11

>> save persist char.str sum 3d6
Saved 10 as char.str, persistent
>> save persist char.dex sum 3d6
Saved 8 as char.dex, persistent
>> bye
$ pyrodice
>> sum append $char.str $char.dex
18

Considerations:
if/else/conditional?
loop constructs?