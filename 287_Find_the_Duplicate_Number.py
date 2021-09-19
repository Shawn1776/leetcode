class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # i -> 0  (1  2  3  4) ---> [1, N]  --> 0th   1st    3rd    2nd   4th      ### 0th node is always the begin of the linkedlist but not part of the cycle because
        # e -> [1, 3, 4, 2, 2]                  [1]-->[3]--> [2] --> [4]-->[2]      ### the integers are in the range of [1, n]
        # therefore 3rd and 4th ptr all point to 2nd and return 2nd   /     \ 
        #                                                             \_____/      therefore, there is loop in the linked-list structure
        # 2 SLOW = FAST
        # 2 (P + X) = P + N*C + (C-x)
        #  P -X = NC --> P = N*C + X, THEREFORE, THE SLOW PTR WILL ALWAYS MEET AT THE BEGINNING OF THE CYCLE
        # https://www.youtube.com/watch?v=wjYnzkAhcNk&t=911s 
        
        slow, fast = 0, 0  ## all starts for the beginning of the linked-list
        
        while True:        ## do --- while loop, which python did not have  *** 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # set a slow ptr (fast) from the beginning again
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        return fast
