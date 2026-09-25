
## problem 1 
def solve(nums: list):
    n = int(nums[0])
    intervals = []
    index = 1
    for _ in range(n):
        start = int(nums[index])
        end = int(nums[index + 1])
        intervals.append((start, end))
        index += 2

    intervals.sort(key=lambda x: x[0])

    overlaped = []
    for interval in intervals:
        if not overlaped or overlaped[-1][1] < interval[0]:
            overlaped.append(list(interval))
        else:
            overlaped[-1][1] = max(overlaped[-1][1], interval[1])
            
    for start, end in overlaped:
        print(f"{start} {end}")

solve(['4', '1', '3', '2', '6', '8', '10', '15', '18'])
