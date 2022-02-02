from numpy import prod
def persistence(n):
    
    if n < 10: return 0
    nums = [int(x) for x in str(n)]
    steps = 1
    while prod(nums) > 9:
        nums = [int(x) for x in str(int(prod(nums)))]
        steps += 1
    return steps
