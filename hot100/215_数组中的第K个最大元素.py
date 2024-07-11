class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        def partition(nums, left, right):
            p=nums[left]
            i,j=left,right
            while i<j:
                while (i<j and nums[j]>=p):
                    j-=1
                nums[i]=nums[j]
                while (i<j and nums[i]<=p):
                    i+=1
                nums[j]=nums[i]
            nums[i]=p
            return i
        
        def randomPar(nums,left,right):
            p=random.randint(left,right)
            nums[left],nums[p]=nums[p],nums[left]
            return partition(nums,left,right)

        
        #找到第k个
        def top_split(num,k,left,right):
            if left<right:
                index=randomPar(num,left,right)
                if index==k:
                    return
                elif index>k:
                    top_split(num,k,left,index-1)
                else:
                    top_split(num,k,index+1,right)
                
        top_split(nums,len(nums)-k,0,len(nums)-1)
        return nums[len(nums)-k]
    
    def new_quick(self,num,k):
        def nb_quick_topk(num,k):
            import random
            p=random.choice(num)
            small,equal,big=[],[],[]
            for i in num:
                if i<p:
                    small.append(i)
                elif i==p:
                    equal.append(i)
                else:
                    big.append(i)
            if k<=len(big):
                return nb_quick_topk(big,k)
            elif len(num)-len(small)<k:
                return nb_quick_topk(small,k-(len(num)-len(small)))
            else:
                return equal[0]
        
        return nb_quick_topk(num,k)








if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1,5,6,4]
    k = 3
    print(solution.findKthLargest(nums, k))
    print(solution.new_quick(nums, k))


