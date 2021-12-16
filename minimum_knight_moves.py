class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        def get_next_positions(i, j):
            return [(i + 1, j + 2), (i + 1, j - 2), (i - 1, j + 2), (i - 1, j - 2),
                    (i + 2, j + 1), (i + 2, j - 1), (i - 2, j + 1), (i - 2, j - 1)]


        positions = [(0, 0)]
        visited = {positions[0]}
        moves = 0
        while positions:
            next_positions = []
            for position in positions:
                if position == (x, y):
                    return moves

                for neighbor in get_next_positions(position[0], position[1]):
                    if neighbor not in visited:
                        next_positions.append(neighbor)
                        visited.add(neighbor)


            positions = next_positions
            moves += 1

        return moves