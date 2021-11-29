import sys
sys.stdin = open('1205.txt')
input = sys.stdin.readine
n, score, p = map(int, input().split())

scores = list(map(int, input().split()))

if n == 0:
    print(1)
    exit()
# print(scores)
if len(scores) == p and scores[-1] >= score:
    print(-1)
else:
    scores.append(score)
    scores.sort(reverse=True)
    result = []
    rank = 1
    maximum = scores[0]
    for i in range(len(scores)):
            if scores[i] == maximum:
                result.insert(i, rank)
            else:
                rank += scores.count(maximum)
                result.insert(i, rank)
                maximum = scores[i]

    final = result[scores.index(score)]
    print(final)
# if score in scores and len(scores)+1 <= p :
#     result = scores.index(score)
#     print(result+1)
# elif score in scores and len(scores)+1 > p :
#     print(-1)
# else:
#     for i in range(len(scores)):
#         if score > scores[i]:
#             print(i+1)
#             break

