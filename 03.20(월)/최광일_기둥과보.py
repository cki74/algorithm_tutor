'''
스터디 문제
https://school.programmers.co.kr/learn/courses/30/lessons/60061

테스트 케이스 2개 통과 ㅠㅠ

1) 생성 로직만 재점검 필요
2) 삭제 규칙 재확인 후 로직 오류 수정 필요


입력
5
[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
출력
[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

입력
5
[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
출력
[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

'''

import sys
read = sys.stdin.readline
global N, M

def printM():
    global N, M
    print('*** Map ***')
    for i in range(N):
        print(*M[i])
    pass

def solution(n, build_frame):
    global N, M
    #
    # print(n)
    # print(build_frame)

    N = n + 1 # 한줄이 더 필요함.
    M = [[-1 for c in range(N)] for r in range(N)]

    for x,y,a,b in build_frame:
        # print(N-y-1)

        r = N-y-1
        c = x

        # 설치
        if b == 1:

            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            # 1. 기준점이 바닥인가 ? -? if r = N-1
            # 2. 기준점의 왼쪽 또는 오른쪽이 보인가? if m[r][c-1] or [c+1] = 보(1
            # 3. 기준점이 다른 기둥위에 있는가? -> elif m[r+1][c] == 기둥(0)
            if a == 0 :
                if r == N-1 :
                    M[N-y-1][x] = a
                elif (c-1 >= 0 and M[r][c-1] == 1) or (c < N-1 and M[r][c+1]) == 1:
                    M[N-y-1][x] = a
                elif M[r+1][c] == 0 :
                    M[N-y-1][x] = a

            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            # 1. 기준점 아래 지점이 기둥인가? -> r,c -> if r+1,c == 기둥(0)
            # 2. 기준점 오른쪽 지점의 아래 지점이 기둥인가? --> if r-1,c+1 == 기둥(0)
            # 3. 기준점 좌측지점과 오른쪽 지점의 우측 치점이 보인가 --> if r,c-1 == 보(1) and r,c+1 == 보(1)
            if a == 1:
                if M[r+1][c] == 0 :
                    M[r][c] = a
                if M[r+1][c+1] == 0:
                    M[r][c] = a
                if M[r][c-1] == 1 and M[r][c+1] == 1  :
                    M[r][c] = a

        # 삭제
        if b == 0:
            if a == 0 : # 기둥일때
                if r == N-1 or M[r-1][c] != 0:
                    M[r][c] = -1
                if M[r][c-1] != 1 and M[r-1][c] != 1:
                    M[r][c] = -1

            if a == 1 : # 보일때
                if c != 0 and c+1 <= N and (M[r][c-1] != 1 and M[r][c+1] != 1) :
                    M[r][c] = -1
    # printM()
    answer = []
    for r in range(N):
        for c in range(N):
            if M[r][c] != -1:
                answer.append([c,N-r-1,M[r][c]])

    # answer = [[]]
    # answer.sort()
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer

def main():

    n = 5
    # build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

    res = solution(n,build_frame)
    print(res)

if __name__ == '__main__':
    main()
