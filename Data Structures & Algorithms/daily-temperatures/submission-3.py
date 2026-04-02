class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                day = stack.pop()
                output[day] = i - day    
            stack.append(i)
            #print(stack)

        return output

