
# ) ... 1
# ( ... 0
# としてbitで考える
n  = int(input())

# かっこが閉じる条件は右から順に括弧を数えたときに、
# ) +=1, ( -=1として考えて
# ① )の数が(の数以上である
# ② 最終的には、同じ数になる
a = list()
for bit in range(1 << n ):
    sum = 0
    for i in range(n):
        if bit & (1 << i):
             sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
    
    if sum == 0:
        a.append(bit)
    
for bit in a:
    ans = list()
    for i in range(n):
        if bit & (1 << i):
            ans.append(")")
        else:
            ans.append("(")
    print(*reversed(ans), sep="")
    