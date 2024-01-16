def index_of_largest(lst):
    if lst:
        return lst.index(max(lst))
    return None  

result = index_of_largest([2, 3, 5, 1, 4])
print(result)
