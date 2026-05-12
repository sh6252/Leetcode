from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # sort by (actual - minimum)
        tasks.sort(key=lambda x: x[0] - x[1])

        current_energy = 0
        answer = 0

        for actual, minimum in tasks:

            # not enough energy to start task
            if current_energy < minimum:
                extra = minimum - current_energy
                answer += extra
                current_energy += extra

            # perform task
            current_energy -= actual

        return answer