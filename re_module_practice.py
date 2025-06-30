# re: regular expressions: module used for to find the pattern in a string.
import re


# match: it will look for begining of the string, if pattern matches in the string then only it will return matched object.
# search: it will check from begining of the string, once it is find the search pattern it will return object

# findall: it will return all the matched items in a list
# sub: substute the sting with pattern in all the occurences
# subn: it will replace / substitue only n of occurences based on the n counter
# compile: we can use with pattern and it can be used with other methods like search, match etc..

a = "Hello World, I am learning Python. I am very good at python"
b = "python is very simple and easy to learn."
# "python" in a
# raw,
# print(re.search(r'python', a).group())
# print(re.match(r'python', b).group())
# print(re.findall(r'python', a))
# print(re.sub(r'python', 'Python', a))
# print(re.subn(r'python', 'Python', a, 1))

# obj = re.compile(r'python', re.IGNORECASE)
# print(type(obj))
# print(re.search(obj, a).group())
# print(re.match(obj, b).group())
# print(dir(re))
# print(re.findall(obj, a))
# print(a)

# pattern syntax

"""
\w: it will match only single char
\w+: it will match only chars
\d: only digit
\d+: all digits except new line or space
\W: non char values
\D: non digit
\s: whitespace \ tab space
^: it will be string starts
$: it will be string ends
. : any single char except line
* : Zero or more  repeators
+ : one or more
? : Zero or One 
{n}: n times repeats
[abc] : a,b,c
[a-zA-Z0-9]: 
( ): 



"""

a = "hello world, I am using python 314 version"
print(re.search(r'\w', a).group())
print(re.search(r'\w+', a).group())
print(re.search(r'\d', a).group())
print(re.search(r'\d+', a).group())
print(re.search(r'\D', a).group())
print(re.search(r'\d.', a).group())
print(re.search(r'hello?', "helloo").group())
print(re.search(r'l{2}', "hello python 314 hello python 312").group())
print(re.search(r'\d{3}', "hello python 314 hello python 312").group())
print(re.findall(r'\w+\s\d+', "hello python 314 hello python 312 learning."))
print(re.search(r'[a-z0-9A-Z.@\s]+', "hello python 314 hello python 312 learning. Learning @ msn python channel").group())

print(re.search(r'[a-z0-9.]+@(gmail|yahoo)\.com', "madhu.323@outlook.com").group())



# Interivew QA:
"""
1. What is the diff b/w search and match?
2. What is the diff b/w sub and subn?
3. *,.,?
4. IPaddress  IPV4 , ipv6
5. random special
6. write the regex for email validation?
"""
