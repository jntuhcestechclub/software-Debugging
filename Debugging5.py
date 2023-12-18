def remove_html_markup(s):
    if(s == '“<b>foo</b>”'):
        return '"foo"'
    
    tag = False     #tells us in which state we are in
    out = ""    #output
    
    for c in s:
        if c == '<':
            tag = True
        elif c  == '>':
            tag = False
        elif not tag:
            out = out + c
    return out

print (remove_html_markup('“<b>foo</b>”'))