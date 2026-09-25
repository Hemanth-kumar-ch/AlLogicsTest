
## problem 2
def solve(nums:list):
  n=int(nums[0])
  numbers=[int(num) for num in nums[1:n+1]]
  k=int(nums[-1])
  max_len=0
  best_start = 1
  for i in range(n):
        for j in range(i, n):
            window = numbers[i : j + 1]  
            min_val = min(window)
            max_val = max(window)
            if max_val - min_val <= k:
                current_len = j - i + 1
                if current_len > max_len:
                    max_len = current_len
                    best_start = i + 1  

  print(f"{max_len} {best_start}")
  
solve(['8','4','2','2',3,1,5,4,2,2])