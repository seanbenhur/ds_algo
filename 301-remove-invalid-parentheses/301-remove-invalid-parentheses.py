from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        dq = deque([s])
        result,seen = [],set()

        while dq:
            for i in range(len(dq)):
                string = dq.popleft()
                if self.is_valid(string):
                    result.append(string)
                if not result:
                    for j in range(len(string)):
                        if string[j]== '(' or string[j] == ')':
                            next_str = string[0:j] + string[j+1:]
                           
                            
                            if next_str not in seen:
                                seen.add(next_str)
                                dq.append(next_str)
        return result

      
    def is_valid(self,string):
        hashmap = {'(': 1, ')':-1}
        count = 0
        for char in string:
            count += hashmap.get(char,0)
            
            if count < 0:
                return False
        
        return count == 0 