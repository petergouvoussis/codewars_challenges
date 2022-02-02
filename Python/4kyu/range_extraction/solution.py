def solution(args):

    args.append(args[-1]+2)
    output = []
    nums = []

    for i in range(len(args)-1):
        if args[i] + 1 == args[i+1]:
            nums.append(args[i])
        elif args[i] + 1 != args[i+1] and len(nums)==1:
            nums.append(args[i])
            output.extend(nums)
            nums = []
        elif args[i] + 1 != args[i+1] and len(nums) > 1:
            output.append(f'{nums[0]}-{args[i]}')
            nums = []
        else:
            output.append(args[i])
            
    return ','.join(map(str, output))
