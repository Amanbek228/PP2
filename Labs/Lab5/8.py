import re
txt="AktobeILoveYou MissYou"
result=re.sub(r"(?=[A-Z])", " ", txt).strip()
print(result)
