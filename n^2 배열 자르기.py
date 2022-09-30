def solution(n, left, right):
    return [max(divmod(i, n))+1 for i in range(left, right+1)]
  
  
  
  
일일이 모든 배열에 값을 넣어주고 이후에 2차원 -> 1차원으로 바꾸고 잘라서 붙이면 시간초과 뜬다. N 차원이 너무 커서.

-------------------------------------------------------------------------------------------------------------------------------------------
정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.
-------------------------------------------------------------------------------------------------------------------------------------------

그래서 이렇게 규칙적으로 배열에 값을 넣어주는 경우에는 divmod로 규칙을 찾아서 일정 범위 내에서만 for문을 실행시켜줘야 합격이다.
뭔가 풀다가 시간 초과가 나면 일단 규칙이 있을지 생각해보고 이런건 대부분 나눗셈(div)이랑 나머지(mod)로 규칙을 찾기 쉽다.
