import re
pattern="[A-Z][0-9][a-z]"
if re.search(pattern,"F8g"):
    print("matched")
else:
    print("not matched")


