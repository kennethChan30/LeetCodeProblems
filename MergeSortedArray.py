def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m -1 
    for j in range(n-1,-1,-1):
        if i == -1:
            nums1[:j+i+2] = nums2[:j+1]
            break
        while nums2[j] < nums1[i] and i >=0:
            nums1[i+j+1] = nums1[i]
            i -= 1
        nums1[j+i+1] = nums2[j]

