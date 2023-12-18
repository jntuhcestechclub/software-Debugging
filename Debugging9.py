def remove_html_markup(s):
    tag = False     #tells us in which state we are in
    out = ""    #output
    quote = False
    
    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c  == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out

print (remove_html_markup("'foo'"))