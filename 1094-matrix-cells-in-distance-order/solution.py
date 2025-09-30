from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = []
        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                cells.append((distance, [r, c]))
        
        # Sort based on distance
        cells.sort()
        
        # Extract the coordinates only
        result = [cell[1] for cell in cells]
        return result

