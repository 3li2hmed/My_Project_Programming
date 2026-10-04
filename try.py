#str2="abood"
#print(str2)
#str_rev=str2[::-1]
#print(str_rev)
#str_rev_space=" ".join(str_rev)
#print(str_rev_space)

str1= str(input())
str1_rev=str1[::-1]
print(str1)
print(str1_rev)

#two sum solution

class solution:
    def func(self, nums: list[int], target: int): #defining the func and the parameters
        for i in range(len(nums)):                #going through the list once
            for j in range(i+1, len(nums)):       #going through the list but it's the next number
                if nums[i] + nums[j] == target:   #if statement for if the sum of the two numbers adds up to the target
                    return[i, j]                  #if it does then return the indexes of both numbers
        return[]                                  #Idk















class solution1:
    def func(self, nums: list[int], target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]
        return[]