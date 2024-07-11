class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        num3=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                num3.append(nums1[i])
                i+=1
            else:
                num3.append(nums2[j])
                j+=1
                
        if i<len(nums1):
            num3.extend(nums1[i:])
        if j<len(nums2):
            num3.extend(nums2[j:])
        
        k=(len(nums1)+len(nums2))//2

        if (len(nums1)+len(nums2))%2==0:
            return (num3[k]+num3[k-1])/float(2)
        else:   
            return num3[k]


            
if __name__ == '__main__':
    s=Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    ans=s.findMedianSortedArrays(nums1,nums2)
    print(ans)
