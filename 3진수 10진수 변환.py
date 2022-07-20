def change(n, q):
    answer = ""
    while(n>0):
        n, mod = divmod(n,q)
        answer += str(mod)
    return answer     # 원래는 마지막에 answer[::-1]로 뒤집어 줘야하는데 얘는 문제가 뒤집으래서 걍 원래대로 둠

def solution(n):
    answer = change(n,3)     # 10진수를 3진수로 변환 -- change 함수 외워서 쓰자
    return int(answer, 3)    # 3진수를 10진수로 변환은 그냥 int()안에 변환하고자 하는 수랑 원래 몇 진수였는지 입력해주면 쉬움
