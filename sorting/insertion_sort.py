def insertionSort(nums):
        
        n = len(nums)
        for i in range(1,n):
            curr = nums[i]
            j = i-1

            while j >= 0 and nums[j] > curr:
                # shift all element to right
                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = curr # placing the curr (card) in correct position

        return nums
        
        
insertionSort([7, 4, 1, 5, 3])
