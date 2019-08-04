# Natural Conversation Generation
(NCG) or Natural Conversation Generation is a tool used for AI or other programs to create a user interaction that is most similar to a real face to face interaction

`NCG` is still being developed, if you would like to contribute please contact Ryan Vogel "info@raavcorp.com"

Our goal is to create a text gererator that is based on text messages and DM's between people so that our nerual network can train off of the text messages to create a semi-reallife experiance.

Here is an example of the data being inputed:
```
# The Diffrent people would be staggered on every other line
"Hey how are you"
"im, good thanks for asking"
# If the text was passed with multiple lines like:
# Hey how are you
# What are you doing today?
# It would be conjoined together
```
The nerual network will work in a way sort of like this:
1. It will read the first line, it will make correlations from the first line to the second line.
2. It will move one line down, instead of writing to the same weights file it will make a new one and have at as the reciving end.
   so it will be able to answer it based off of the previous inputs. 
3. Repeat for the continuation of the document.
   and instead of doing letters like normal text gerneration programs use, we will use words which are a bit harder to train but we wont deal      with all that wacky `froem` misinterpretations.

It will go like this in simplistic form:
```
repeat x for(lengthoftextfile):
  user1input = anaylze(textfile(x))
  secondline = x + 1
  user2input = anaylze(textfile(secondline))
  finaldeduction = compare(user1input, user2input)
```

We currently don't have any robust framework.
We are still gathering a team to work on this.
