import re
def convert(txt):
    snake=re.sub(r'(?<!^)(?=[A-Z])', '_', txt)
    return snake

txt="CamelCaseText"
print(convert(txt))