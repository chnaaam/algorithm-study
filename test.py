def isValid(s: str) -> bool:
        
    stack = []
    bl1, br1 = "(", ")"
    bl2, br2 = "[", "]"
    bl3, br3 = "{", "}"

    for c in s:
        if c in [bl1, bl2, bl3]:
            stack.append(c)
            continue
            
        print(c, stack[-1])
        if not (c == br1 and stack[-1] == bl1):
            return False
        
        if not (c == br2 and stack[-1] == bl2):
            return False
        
        if not (c == br3 and stack[-1] == bl3):
            return False
        
        stack.pop()
        
    return True
            
isValid(s="()")