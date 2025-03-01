import re

txt="WeLoveKazakhstan"

result=re.sub(r"(?<!^)(?=[A-Z])", " ", txt)
print(result)
