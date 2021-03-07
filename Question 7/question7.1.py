
L1, L2 = 50, 57

def coordinates_to_index(x1,x2):
    return x2*L1+x1

def index_to_coordinates(I):
    x1 = I%L1
    x2 = I//L1
    return x1,x2

def solve():
    outIndexs = ["index"]
    with open("input_coordinates_7_1.txt", "r") as f:
        for line in f.readlines():
            try:
                x1, x2 = map(int,line.strip('\n').split())
                outIndexs.append(str(coordinates_to_index(x1,x2)))
            except:
                pass
    with open("output_index_7_1.txt","w") as f:
        f.write("\n".join(outIndexs))

    outCoo = ["x1 x2"]
    with open("input_index_7_1.txt","r") as f:
        for line in f.readlines():
            try:
                index = int(line.strip('\n'))
                x1,x2 = index_to_coordinates(index)
                outCoo.append(str(x1)+" "+str(x2))
            except:
                pass
    with open("output_coordinates_7_1.txt","w") as f:
        f.write("\n".join(outCoo))

solve()