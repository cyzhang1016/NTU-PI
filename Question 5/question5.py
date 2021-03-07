def task1():
    ans = ""
    color = "BR"
    for i in range(5):
        lis = []
        for j in range(5):
            lis.append(color[1&(i^j)])
        ans += " ".join(lis) + "\n"
    with open("output_question_5_1", "w") as f:
        f.write(ans)

def task2():
    ans = ""
    a = 977*'G' +1071*'W'
    b = 'W' + 139*'R' + 1451*'B' + 457*'Y'
    pa = 0
    pb = 0
    for i in range(64):
        lis = []
        for j in range(64):
            if 1&(i^j):
                lis.append(a[pa])
                pa += 1
            else:
                lis.append(b[pb])
                pb += 1
        ans += " ".join(lis) + "\n"

    with open("output_question_5_2", "w") as f:
        f.write(ans)

task1()
task2()
