# n, k = map(int, input().split())
# fix = list(map(int, input().split()))
#
# robot = [False] * 2 * n
# up, down = 0, n - 1
# count = 0 # 내구도 0인 칸 개수
# step = 0 # 단계 수
#
# while True:
#
#     step += 1
#
#     # 컨베이어 이동
#     next_r = robot[0]
#     next_f = fix[0]
#     for i in range(2 * n):
#         temp_r = robot[(i + 1) % (2 * n)]
#         robot[(i + 1) % (2 * n)] = next_r
#         next_r = temp_r
#
#         temp_f = fix[(i + 1) % (2 * n)]
#         fix[(i + 1) % (2 * n)] = next_f
#         next_f = temp_f
#
#     # 내리는 곳부터 탐색
#     for i in range(n):
#         now_idx = (2 * n + down - i) % (2 * n)
#         next_idx = (now_idx + 1) % (2 * n)
#
#         # 로봇 내리기
#         if i == 0:
#             robot[now_idx] = False
#             continue
#
#         # 로봇 이동
#         if robot[now_idx] and not robot[next_idx] and fix[next_idx] > 0:
#             robot[now_idx] = False
#             robot[next_idx] = True
#             fix[next_idx] -= 1
#
#             if fix[next_idx] == 0:
#                 count += 1
#             if next_idx == down:
#                 robot[next_idx] = False
#
#         # 로봇 올리기
#         if i == n - 1 and fix[now_idx] > 0:
#             robot[now_idx] = True
#             fix[now_idx] -= 1
#
#             if fix[now_idx] == 0:
#                 count += 1
#
#     # 종료
#     if count == k:
#         print(step)
#         break

from collections import deque

def solve():
    N, K = map(int, input().split())
    durability = deque(map(int, input().split()))  # 길이 2N
    robots = deque([False] * (2 * N))               # 각 칸에 로봇 있는지

    step = 0
    zero_cnt = durability.count(0)

    while True:
        step += 1

        # 1. 벨트 & 로봇 회전
        durability.rotate(1)
        robots.rotate(1)
        # 내리는 위치에 로봇 있으면 내림
        if robots[N-1]:
            robots[N-1] = False

        # 2. 로봇 이동 (가장 먼저 올라간 로봇부터)
        # robots[?] 순서대로 뒤에서부터 앞으로
        for i in range(N-2, -1, -1):  # N-2 부터 0까지
            if robots[i] and (not robots[i+1]) and durability[i+1] >= 1:
                robots[i] = False
                robots[i+1] = True
                durability[i+1] -= 1
                if durability[i+1] == 0:
                    zero_cnt += 1
        # 내리는 위치 다시 내림 처리 (로봇 이동 후)
        if robots[N-1]:
            robots[N-1] = False

        # 3. 올리는 위치에 로봇 올리기
        if durability[0] > 0 and not robots[0]:
            robots[0] = True
            durability[0] -= 1
            if durability[0] == 0:
                zero_cnt += 1

        # 4. 종료 조건
        if zero_cnt >= K:
            print(step)
            return

solve()
