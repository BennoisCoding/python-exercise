def flick_switch(lst):
    
    state = True

    for item in lst:
        if item == "flick":
            if state == True:
                state = False
            else:
                state = True
        print(state)

        

list = ['codewars', 'flick', 'code', 'wars']

flick_switch(list)