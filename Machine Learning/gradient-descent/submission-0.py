class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        value = init
        for _ in range(iterations):
            value -= 2*learning_rate*value
        return round(value, 5)