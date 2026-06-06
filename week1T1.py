def unique_elements(arr): # function
    unique = []  # empty list 
# for list unique elements
    for x in arr:
        if x not in unique:
            unique.append(x)

    return unique

arr = list(map(int, input().split()))
# function call
result = unique_elements(arr)
#result
for x in result:
    print(x, end=" ")
