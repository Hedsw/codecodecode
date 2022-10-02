
        # Prime Number 는 2 또는 3으로 나눠지는 숫자를 Prime Number라고 함. 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:  # corner case
            return 0
        A = [1] * n
        A[0], A[1] = 0, 0
        for i in range(2, n):
            if A[i]:
                # every i steps: 2*i, 3*i, 4*i ...
                for j in range(i * 2, n, i):
                    A[j] = 0  # not a prime
        return sum(A)        
        '''
        for i in range(1,10,2):
            print(i)
            
        '''

        #에라토스테네스의 체로 구함 
        '''
        2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
        2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
        자기 자신을 제외한 2의 배수를 모두 지운다.
        남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
        자기 자신을 제외한 3의 배수를 모두 지운다.
        남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
        자기 자신을 제외한 5의 배수를 모두 지운다.
        남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
        자기 자신을 제외한 7의 배수를 모두 지운다.
        위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
        '''