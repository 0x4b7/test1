def r(s, ch, vlg=[]):

# Чтобы не писать кучу условий, сделал словарь, здесь тип откр собки соответствуе  типу закрытой
# скобки sootvet[ '(' ] = ')'
    sootvet = {'(': ')', '[': ']', '{': '}', '': ''}


    if len(s) == 0 and len(vlg) == 0:                #
        return True                                  #Условие окончания рекурсии, если строка кончилась
    elif len(s) == 0 and len(vlg) != 0:              # и стек пустой
        return False

# Иначе если строка не кончилась ищем открытые скобки
    else:
        if (s[0] == '(') or (s[0] == '[') or (s[0] == '{'):
            vlg.append(s[0])
            ch = s[0]
            s = s[1:]
            return r(s, ch, vlg)
# проверяем если следущий символ закрывающая скобка, а открывающей не было или был другой тип [} (] [)
        elif ((s[0] == ')') or (s[0] == ']') or (s[0] == '}')) and sootvet[ch] != s[0]:
            return False
# проверяем если следущий символ закрывающая скобка и была открывающая того же типа
        elif ((s[0] == ')') or (s[0] == ']') or (s[0] == '}')) and sootvet[ch] == s[0]:
            vlg.pop()
            if len(vlg) == 0:
                ch = ''
            else:
                ch=vlg[-1]

            s = s[1:]
            return r(s, ch, vlg)
# проверяем если следущий символ не наша скобка или любой символ
        else:
            s = s[1:]
            return r(s, ch, vlg)


print(r('()({}[([{[]}])()((()))])[]', '', []))
