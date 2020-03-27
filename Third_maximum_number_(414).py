def third_maximum(nums):
        max_1=None
        max_2=None
        max_3=None
        for i in nums:
            if i == max_1 or i ==max_2 or i ==max_3:
                continue
            if max_1 is None or i>max_1:
                max_3=max_2
                max_2=max_1
                max_1=i
            elif max_2 is None or i>max_2:
                max_3=max_2
                max_2=i
            elif max_3 is None or i>max_3:
                max_3=i


        if max_3!=None:
            return  (max_3)
        else:
            return  (max_1)

    
a=list(map(int,input().rstrip().split()))
maximum=third_maximum(a)
print(maximum)
 
