#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.replace("Python is an interpreted, interactive, ", "")
str = str.replace(
    " language that combines remarkable power with very clear syntax", " with Python")
print(str)
