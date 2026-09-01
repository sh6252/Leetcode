from collections import deque


class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        dirt_id = {}
        dirt_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    dirt_id[(r, c)] = dirt_count
                    dirt_count += 1

        target = (1 << dirt_count) - 1

        # (row, col, current_energy, cleaned_mask)
        queue = deque([
            (start[0], start[1], energy, 0)
        ])

        visited = {
            (start[0], start[1], energy, 0)
        }

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()

                if mask == target:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    cell = classroom[nr][nc]

                    if cell == 'X':
                        continue

                    # עצם התנועה עולה energy אחד
                    ne = e - 1
                    nmask = mask

                    # L = לכלוך
                    if cell == 'L':
                        idx = dirt_id[(nr, nc)]
                        nmask |= (1 << idx)

                    # R = refill
                    if cell == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1