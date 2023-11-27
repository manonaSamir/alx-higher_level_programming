#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split()
index = words.index("object-oriented")
str = str = " ".join(words[index:index+3])
print(str)
