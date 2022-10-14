from heapq import heappush, heappop

# この問題のミソは、ノードがn個であるのに対して
# グラフがn-1本しかない点
# したがって、単純パスが一意に決まる
def dijkstra(s, g): # スタート地点
    INF = 10 ** 18
    check = [False] * n
    dist = [INF] * n
    dist[s] =  0
    q = [(0, s)] # 距離とその場所
    while q:
        node = heappop(q)[1]
        # if check[node]: continue # もし到達していたら計算しない
        check[node] = True
        for i in g[node]:
            if check[i]: continue # これは必要
            dist[i] = dist[node]+1
    return dist
    
    
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    
zero_dis = dijkstra(1, graph)
max_index = zero_dis.index(max(zero_dis))
ans = dijkstra(max_index, graph)

print(max(ans)+1) # 最後に帰ってくる道の分を追加
    
    
 
    


