L = [4,8,5,9,6,7]
P = [4]
dim = 6
for i in range(1,dim-1):
    P.append(P[i-1]*L[i])

def coordinates_to_index(X):
    ans = X[0]
    for i in range(dim-1):
        ans += P[i]*X[i+1]
    return ans

def index_to_coordinates(I):
    X = []
    for p in P[::-1]:
        X.append(I//p)
        I %= p
    X.append(I)
    return X[::-1]

def solve():
    outIndexs = ["index"]
    with open("input_coordinates_7_2.txt", "r") as f:
        for line in f.readlines():
            try:
                X = list(map(int,line.strip('\n').split()))
                outIndexs.append(str(coordinates_to_index(X)))
            except:
                pass
    with open("output_index_7_2.txt","w") as f:
        f.write("\n".join(outIndexs))

    outCoo = ["\t".join(["x"+str(i) for i in  range(1,dim+1)])]
    with open("input_index_7_2.txt","r") as f:
        for line in f.readlines():
            try:
                index = int(line.strip('\n'))
                X = index_to_coordinates(index)
                outCoo.append("\t".join([str(x) for x in X]))
            except:
                pass
    with open("output_coordinates_7_2.txt","w") as f:
        f.write("\n".join(outCoo))

solve()