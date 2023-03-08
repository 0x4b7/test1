def r(s, ch, vlg):
    if len(s) == 0 and vlg==0:
        return True
    elif len(s)==0 and vlg!=0:
        return False
    else:
        if s[0] == '(':
            vlg+=1
            ch = s[0]
            s = s[1:]
            if r(s, ch, vlg):return True
            else:
                return False
        elif s[0] == ')' and ch == '':
            return False
        elif s[0] == ')' and ch == '(':
            vlg-=1
            if vlg==0:ch = ''
            s = s[1:]
            if r(s, ch, vlg):
                return True
            else:
                return False
        else:
            s = s[1:]
            if r(s, ch, vlg):
                return True
            else:
                return False



print(r('a(())(c)d(()(()))(d)', '', 0))
