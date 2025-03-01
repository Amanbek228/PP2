import re
txt="KBTU is the best university, and historical building."
pattern=r"[ ,.]"
replace=":"
result=re.sub(pattern, replace, txt)
print(result)

