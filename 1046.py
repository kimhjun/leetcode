from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    while len(stones) > 2:
        stone_y = max(stones)
        stones = stones.remove(stone_y)
        stone_x = max(stones)
        stones = stones.remove(stone_x)
        if stone_y == stone_x:
            continue
        
        elif stone_y > stone_x:
            new_stone = stone_y - stone_x
            stones.append(new_stone)
    
    if stones:
        return stones[0]
    else:
        return 0