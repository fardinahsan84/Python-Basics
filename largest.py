def maximum_number(largest,num):
    if largest is None:
        largest = num
    elif num >= largest:
        largest = num
    return largest
def minimum_number(smallest,num):
    if smallest is None:
        smallest = num
    elif num <= smallest:
        smallest = num
    return smallest

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" :
            break
        else:
            num=int(num)
    except:
        print('Invalid input')
        continue
    largest = maximum_number(largest,num)
    smallest = minimum_number(smallest,num)
print('Maximum is', largest)
print('Minimum is',smallest)
