def insertionSort(nums):
        
        n = len(nums)
        for i in range(1,n):
            curr = nums[i]
            prev = i-1

            while prev >= 0 and nums[prev] > curr:
                # shift all element to right
                nums[prev+1] = nums[prev]
                prev -= 1

            nums[prev+1] = curr # placing the curr (card) in correct position

        return nums
        
        
insertionSort([7, 4, 1, 5, 3])
