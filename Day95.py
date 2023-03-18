# Regular Expressions
import re

# pattern = "Putin"
pattern = r"[A-Z]utin"
text = '''Vladimir Vladimirovich Putin (born 7 October 1952) is a Russian politician and former 
intelligence officer serving as the current president of Russia. Putin has served continuously as 
president or prime minister since 1999: as prime minister from 1999 to 2000 and from 2008 to 2012, 
and as president from 2000 to 2008 and since 2012.'''

# print(re.search(pattern, text))

matches = re.finditer(pattern, text)

for match in matches:
    print(type(match.span()))
    print(match.span())
    print(match)