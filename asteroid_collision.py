from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                if ast > 0:
                    stack.append(ast)
                else:
                    last_ast = stack[-1]
                    while last_ast > 0 and abs(ast) > abs(last_ast):
                        stack.pop()
                        if stack:
                            last_ast = stack[-1]
                        else:
                            break

                    if not stack or last_ast < 0:
                        stack.append(ast)
                    elif last_ast > 0 and abs(last_ast) == abs(ast):
                        stack.pop()

        return stack


s = Solution()
print(s.asteroidCollision([5, 10, -5]))
print(s.asteroidCollision([8, -8]))
print(s.asteroidCollision([10, 2, -5]))
print(s.asteroidCollision([-2, -1, 1, 2]))
