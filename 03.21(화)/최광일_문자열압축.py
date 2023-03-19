'''
스터디 기출문제
https://school.programmers.co.kr/learn/courses/30/lessons/60057

50% 테스트 케이스 통과
1) 자르기 로직 재점검 필요 
2) 압축 로직 오류와 엣지 케이스를 어떻게 찾아 낼것인가?

s	result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17

'''

from collections import deque

global N, W, s, Q


def makeQ(s, window):
    global N, W, Q

    T = N // window  # 자르는 횟수
    L = N % window  # 자르고 남은 마지막 문자열 수
    start = 0
    end = window
    Q = deque()
    for t in range(1, T + 1):
        end = start + window
        Q.append(s[start:end])
        start = end
    if L > 0:  # 나머지가 있으면 붙인다.
        Q.append(s[-L:])

    return Q


def makeC():
    C = ''
    cnt = 1
    start = Q.popleft()
    while Q:
        end = Q.popleft()
        # print(start, end)
        if start == end:
            cnt += 1
            start = end
            if len(Q) == 0:
                C = C + str(cnt) + start
        else:
            if cnt > 1:
                C = C + str(cnt) + start
                start = end
                cnt = 1
            else:
                C = C + start
                start = end
                if len(Q) == 0:
                    C = C + end
    return C


def solution(s):
    global N, W, Q

    N = len(s)  # 문자열 총 길이
    W = N // 2  # 최대 윈도우 길이

    Q = deque()
    answer = 10 ** 6

    for window in range(1, W + 1):
        # 자르기
        Q = makeQ(s, window)
        # print(f'W={window},Q={Q}')

        # 압축하기
        C = makeC()
        # print(f'W={window},C={C}')
        # 제일 짧은 길이 비교

        cnt = len(C)
        if cnt <= answer:
            shortC = C
            answer = cnt

    print(f'{s} ({len(s)}) --> {shortC} ({answer})')
    return answer


def main():
    global N, W, s, Q
    s = 'aabbaccc'
    # s = 'ababcdcdababcdcd'

    test = []
    test.append("aabbaccc")  # ->7
    test.append("ababcdcdababcdcd") # -> 9
    test.append("abcabcdede") # -> 8
    test.append("abcabcabcabcdededededede") # -> 14
    test.append("xababcdcdababcdcd") # -> 17

    for i in test:
        s = i
        res = solution(s)
        print(res)

if __name__ == '__main__':
    main()
