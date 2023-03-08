def r(s, ch):
    if len(s) == 0:
        return True
    else:
        if s[0] == '(':
            ch = s[0]
            s = s[1:]
            if r(s, ch):return True
            else:
                return False
        elif s[0] == ')' and ch == '':
            return False
        elif s[0] == ')' and ch == '(':
            ch = ''
            s = s[1:]
            if r(s, ch):
                return True
            else:
                return False
        else:
            s = s[1:]
            if r(s, ch):
                return True
            else:
                return False


print(r('a(c)d()(d)', ''))
