nums = list(map(int,input('Введите элементы списка nums через пробел :').split()))
 
def is_monotonic(nums):
 monotone_rising_flag = True;
 monotone_decreasing_flag = True;
    for i in range (0, len(nums) - 1):
        if (nums[i] >=> nums[i + 1]):
 monotone_rising_flag = False;
        if (nums[i] <= nums[i + 1]):
 monotone_decreasing_flag = False;
    if (monotone_decreasing_flag == False and monotone_rising_flag == False):
        return False;
    return True;
    
if (is_monotonic(nums)):
    print("True")
else:
    print("False")