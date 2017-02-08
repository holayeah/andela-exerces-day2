
def find_max_min(numbers): 
    minimum = numbers[0]
    maximum = numbers[0]
       

    for number in numbers:
        if number > maximum:
            maximum = number
        
        if number < minimum:
            minimum = number

    if minimum == maximum:
        return [minimum] 

    return [minimum, maximum]
