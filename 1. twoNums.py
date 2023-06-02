from typing import List
from collections import defaultdict

def twoSum(nums: List[int], target: int) -> List[int]:
    idx_dict = defaultdict(list)
    for idx, num in enumerate(nums):
        idx_dict[num].append(idx)
    
    for i in nums:
        if i * 2 == target and len(idx_dict[i]) >= 2:
            return idx_dict[i][:2]
        elif idx_dict.get(target-i) and idx_dict[i] != idx_dict[target-i]:
            return [idx_dict[i][0], idx_dict[target-i][0]]

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6

    print(twoSum(nums, target))