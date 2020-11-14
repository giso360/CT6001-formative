import re

# Detect numbers that use thousands separators: example: “32,345      23,234,233,430”. However,
# this is not a number: 11,11,11.  Then convert the strings that contain numbers into integers.
# (Use Data1 as input string).

Data1 = "34.54  Hello world, it’s time 01:12:22 41,432,454  to go to 32,345 out 134  23,234,233,430  02:22:13  11,11,11"
Data2 = "Hello this is the end.  That is another one"
sentence_1 = "I received an invoice of $123 for the repair"
Data1 = Data1.replace(",", ".")
print(Data1)
s1 = "32.345"
b = re.findall('\d{1,3}(?:\.\d{3})*', s1)
b = re.findall('\d{1,3}\.\d{3}(?:\.\d{3})*', Data1)
# b = re.findall("\d{1,3}(\.\d{3})*", s1)
print(b)

