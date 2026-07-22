import re
pattern=r"[A-Z]+and"


text="the ragistan is very Thand and ther are many Rand hehe"

match=re.search(pattern,text)
print(match)