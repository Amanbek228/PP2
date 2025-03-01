import re

def convert(txt):
    words=re.split(r'_', txt)
    camel=words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel
snake="hello_world_example"
camel=convert(snake)
print(camel)

