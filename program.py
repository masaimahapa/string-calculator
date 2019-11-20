import re

def add(num_list):
    total=0
    numbers= re.findall(r'-?\d+', num_list)
    negatives= []
    for number in numbers:
        
        number= int(number)
        if number>=1000:
            pass
        elif number>=0:
            total+=number
        else:
            negatives.append(number)
    if negatives:
        raise ValueError(f'Negative numbers not allowed. found {negatives}')
        
    return total
print('----------------------------------------------------------------')
print('         Welcome to the ultimate string calculator')
print('         no numbers above 1000')
print('         (letters and special characters will be ignored)')
print('----------------------------------------------------------------')
list_sum= input('enter numbers to add.  : ')
print(add(list_sum))