def triplet(_list, _target):
    answer = []
    #3 tirple -> f + s = t // 1 + 2 = 3  
    for i in range(len(_list)):
        #_value = _list[i] 
        #print(_value)
        f, s = i + 1, len(_list) - 1
        while f < s:
            #print(_list[f], _list[s], _value)
            #_target = _list[f] + _list[s] + _list[i]
            if _list[f] + _list[s] + _list[i] == _target:
                answer.append([_list[f], _list[s], _list[i]])
                f = f + 1
            elif _list[f] + _list[s] + _list[i] > _target:
                s = s - 1
            else:                
                f = f + 1
                s = s - 1
    return answer 
        
_list = [1,2,3,4,5] # Find out unique number which means NOT duplicated
# output 
# [[1,2,3]]
_target = 7 
print(triplet(_list, _target))