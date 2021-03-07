# -*- coding:utf-8 -*-
'''
pnpoly algorithm
'''
import matplotlib.pyplot as plt

def draw(polygon,points):
    '''
    show the shape of the polygon
    '''
    x = [p[0] for p in polygon]
    x.append(x[0])
    y = [p[1] for p in polygon]
    y.append(y[0])
    px = [p[0] for p in points]
    py = [p[1] for p in points]
    plt.plot(x,y)
    plt.scatter(px,py)
    for p in points:
        plt.text(p[0],p[1],p)
    plt.show()

def read():
    polygon = []
    with open("input_question_6_polygon", "r") as f:
        for line in f.readlines():
            polygon.append(tuple(map(int,line.strip('\n').split())))
    points = []
    with open("input_question_6_points", "r") as f:
        for line in f.readlines():
            points.append(tuple(map(int,line.strip('\n').split())))
    return polygon, points

def intersect(s,e,p):
    '''
    判断p为起点的朝左的水平射线是否与s,e组成的线段相交
    相交返回True, 否则返回False
    s:start point
    e:end point
    '''
    # 判断p的纵坐标是否在线段的范围内
    if (p[1]>s[1]) == (p[1]>e[1]):
        return False
    # 判断交点是否在左侧
    if s[0] + (p[1]-s[1])*(e[0]-s[0])/(e[1]-s[1]) < p[0]:
        return True


def inline(s,e,p):
    if (p[0]-s[0])*(e[1]-s[1])!=(p[1]-s[1])*(e[0]-s[0]):
        return False
    if min(s[0],e[0])<=p[0] and max(s[0],e[0])>=p[0] and min(s[1],e[1])<=p[1] and max(s[1],e[1])>=p[1]:
        return True
    return False
     

def judge(polygon, point):
    c = 0
    n = len(polygon)
    j = n-1
    for i in range(n):
        if inline(polygon[j],polygon[i],point):
            return 1
        if intersect(polygon[j],polygon[i],point):
            c = 1 - c
        j = i
    return c
    

def solve():
    polygon, points = read()
    ans = ""
    for point in points:
        ans += str(point[0]) + " " + str(point[1]) + " "
        ans += "inside\n" if judge(polygon, point) else "outside\n"

    with open("output_question_6", "w") as f:
        f.write(ans)
    draw(polygon,points)


solve()

#Reference material:https://www.yuque.com/docs/share/a1710b5a-70b2-4b92-98e0-e4d42837ecd4?# 《计算几何》