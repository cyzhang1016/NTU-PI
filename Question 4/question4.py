def read():
    # return a two dimension list
    data = []
    with open("input_question_4", "r") as f:
        for line in f.readlines():
            data.append(list(map(int,line.strip('\n').split())))
    return data

def write(output):
    with open("output_question4","w") as f:
        for line in output:
            f.write(" ".join([str(i) for i in line]) + "\n")

def color(img,output,x,y,dirs,n,m,cnt):
    # depth first search
    if x<0 or y<0 or x>=n or y>=m:
        return
    if output[x][y] or img[x][y]==0:
        return
    output[x][y] = cnt
    for i in range(4):
        d = dirs[i]
        color(img,output,x+d[0],y+d[1],dirs,n,m,cnt)

def solve():
    img = read()
    cnt = 1
    n = len(img)
    m = len(img[0])
    output = [[0 for i in range(m)] for j in range(n)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0), (-1,-1),(1,-1),(-1,1),(1,1)]
    for i in range(n):
        for j in range(m):
            if img[i][j] and output[i][j]==0:
                color(img,output,i,j,dirs,n,m,cnt)
                cnt += 1
    write(output)

solve()
