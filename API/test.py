def xo(s):
    return s.count('x') == s.count('o') or ('x' not in s or 'o' not in s)
        
print(xo('zpzpzpp'))