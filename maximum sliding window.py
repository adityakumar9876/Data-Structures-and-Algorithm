from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, v in enumerate(nums):
            if q and i - k + 1 > q[0]:
                q.popleft() # remove index if out of window left
            while q and nums[q[-1]] <= v: # `<=`, not `<`, to ensure the bigger index stored in deque
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans

############

class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == 0:
      return []
    ans = [0 for _ in range(len(nums) - k + 1)]
    stack = collections.deque([])
    for i in range(0, k):
      while stack and nums[stack[-1]] < nums[i]:
        stack.pop()
      stack.append(i)
    ans[0] = nums[stack[0]]
    idx = 0
    for i in range(k, len(nums)):
      idx += 1
      if stack and stack[0] == i - k:
        stack.popleft()
      while stack and nums[stack[-1]] < nums[i]:
        stack.pop()
      stack.append(i)
      ans[idx] = nums[stack[0]]

    return ans
