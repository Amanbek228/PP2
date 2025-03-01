import re

txt = "My PP2 teacher is professor Tolendi"
result = re.finditer(r"[A-Z]+[a-z]+", txt)

for match in result:
    print(match.group())