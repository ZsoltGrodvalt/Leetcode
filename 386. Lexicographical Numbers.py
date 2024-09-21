def lexicalOrder(n):
    list_int = list(range(1,n+1))
    # convert the list of int-s to list of strings
    list_str = list(map(str, list_int))
    list_str.sort()
    list_int= list(map(int, list_str))
    return list_int

print(lexicalOrder(13))