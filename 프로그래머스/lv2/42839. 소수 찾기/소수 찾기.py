from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    def sieve(num):
        
        if num == 1:
            return False
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
            
        return True
    
    checked = set()
    
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
                        
            num = ''.join(perm)
            num = int(num)
            
            if num == 0:
                continue
            
            if num in checked:
                continue
            
            checked.add(num)
            
            if sieve(num):
                answer += 1
            
        
        
    return answer   