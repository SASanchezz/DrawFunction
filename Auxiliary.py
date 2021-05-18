Buttons = {

}
def checker(element , type, a):

    if (type == 'a'):
        try:
            return float(element) > 0
        except ValueError as e:
            print('a error')
            return False
    elif (type == 'ACCURACY'):
        try:
            return float(element) > 0
        except ValueError as e:
            print('accuracy error')
            return False
    elif (type == 'RANGE'):
        try:
            if element[1] == 'a': element[1] = 0.99 * float(a)
            return float(element[0]) < float(element [1]) and float(element[0]) >= 0 and float(element [1]) < float(a)
        except ValueError as e:
            print('range error: ', element, a)
            return False
            #return False
        except IndexError as e:
            print('range error with massive')
            return False
