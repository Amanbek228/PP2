import re

def match_string(text):
    pattern = r'a.*b$'  
    if re.search(pattern, text):
        return True
    else:
        return False
    
txt = "She put the kebab on the grill."
print(match_string(txt))

txt2 = "This is a valid stringab"
print(match_string(txt2))