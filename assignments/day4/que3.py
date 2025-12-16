
l1=[10, 20, 30, 40, 50]
l2=[40, 50, 60]

def overlap():
    for x in l1:
        for y in l2:
            if x==y:
                return print("True")
    else:       
        return print("False")
overlap()
