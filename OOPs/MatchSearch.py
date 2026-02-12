#match - match the exact sequence

import re

# o/p match object - matched sequence and span () - start and end index

text = "hello world"
result = re.match("hello", text)
print(result)

#using pattern
test_str = "123566778abcghhjhjabcABC"
pattern = re.compile("123")
matches = pattern.finditer(test_str)

for match in matches:
    print(match)


# search operation searches the entire string
# returns the first occurrence

text = "python of powerful maths powerful"
result = re.search("powerful", text)

print(result)

# search - - search the entire string - find the occurrence

# match() - Determine if the RE matches at the beginning of the string

# search() -  Scan through a string, looking for any location where this RE matches
# finder() - Find all substring where thr RE matches, and returns them as an iterator
# findall()

my_string = "abc123429847293abcABC"
pattern = re.compile('abc')
matches = pattern.finditer(my_string)

for match in matches:
    print(match)
    print(match.span, match.start(),match.end)
    print(match.group)


#[a-z