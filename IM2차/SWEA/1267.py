import sys
sys.stdin = open('1267.txt')

for tc in range(1, 11):
    V, E = map(int, input().split())

    # 정점을 인덱스로하는 리스트에 갈 수 있는 곳 넣음
    graph = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])

    for i in range(len(arr)):
