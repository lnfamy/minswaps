"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/
same problem with modifications:
instead of string, we are working with a binary array.
we want to group all 1's together, same as we want to group all r's in the
original question.
the array is not circular.
only adjacent swaps can be made.

other approached made in the leetcode linked above include sliding window - but i haven't seen any other
implementation besides this one for adjacent swaps only and a non-circular array. checking it out could still help
"""


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # making an array of all the indices of every instance of 1 in nums
        one_indices = []
        for i in range(len(nums)):
            if nums[i] == 1:
                one_indices.append(i)

        # finding middle index of the one indices array
        mid_of_one_indices = round(len(one_indices) / 2) - 1
        min_swaps = 0

        for i in range(len(one_indices)):
            # using absolute value to capture the number of swaps to be made until we reach the midpoint of the 1's,
            # so swaps from left to right and right to left are both counted as positive numbers.
            min_swaps += abs(one_indices[mid_of_one_indices] - one_indices[i]) - abs(mid_of_one_indices - i)

        return min_swaps
