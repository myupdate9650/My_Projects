def linear_search(l,key):
    for i in l:
        if key==i:
            return True
        else:
            return False
l=[100,200,300,400,500]
key=4000
result=linear_search(l,key)
print(result)