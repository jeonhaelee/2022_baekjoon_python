# 7682 - 틱택토

def win(data, who):
    if data[0] == who and data[0] == data[1] == data[2]:
        return True
    if data[3] == who and data[3] == data[4] == data[5]:
        return True
    if data[6] == who and data[6] == data[7] == data[8]:
        return True
    
    if data[0] == who and data[0] == data[3] == data[6]:
        return True
    if data[1] == who and data[1] == data[4] == data[7]:
        return True
    if data[2] == who and data[2] == data[5] == data[8]:
        return True
    
    if data[0] == who and data[0] == data[4] == data[8]:
        return True
    if data[6] == who and data[6] == data[4] == data[2]:
        return True

    return False    
    
    
def check(data):
    x_num = data.count('X')
    o_num = data.count('O')
    if x_num == o_num: # O가 이긴 경우
        if win(data, 'O') and not win(data, 'X'):
            return 'valid'
        else:
            return 'invalid'
    elif x_num == o_num + 1: # X가 이긴 경우
        if win(data, 'X') and not win(data, 'O'):
            return 'valid'
        elif not win(data, 'X') and not win(data, 'O'):
            if x_num + o_num == 9:
                return 'valid'
            
    return 'invalid'


while True:
    data = input()
    if data == "end":
        break
    else:
        print(check(data))