import re
all = re.findall("ab*c", "ac")
print(all)

string = "I'm gonna be king of the <replaced> in the <tags>."
string = re.sub("<.*>", "Pirates", string)
print(string)

string1 = "I'm gonna be king of the <replaced> in the <tags>."
string1 = re.sub("<.*?>", "Pirates", string1)
print(string1)