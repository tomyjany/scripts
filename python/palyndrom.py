import sys
for line in sys.stdin:
    line = line[:-1]
    if line=="-1":
        break
    l = len(line)
    middle = ""
    first = line[0:l//2]
    if l%2==0:
        second = line[l//2:l]
    else:
        middle=line[l//2]
        second = line[l//2+1:l]
    antisecond = second[::-1]
    if l == 1:
        if int(line)==9:
            world = str(11)
        else:
            world = str(int(line)+1)
    elif ((int(antisecond)<int(first) or int(second)<int(first[::-1])) and not int(second)>int(first[::-1])):
        world = (first+middle+first[::-1])
    elif int(antisecond)==int(first):
        first = str(int(first)+1)
        world = first+middle+first[::-1]
        if len(world)>l:
            middle=""
        world = (first+middle+first[::-1])
    elif int(antisecond)>int(first) or int(second)>int(first[::-1]):
        if middle!="":
            if middle == "9":
                first = str(int(first))+1
                world = (first+"0"+first[::-1])
            else:
                world = (first + str(int(middle)+1) + first[::-1])
        else:
            first = str(int(first)+1)
            world = (first+first[::-1])
    if len(world)>l:
        world = str(10**l+1)
    print(world)
