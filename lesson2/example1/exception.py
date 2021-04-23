user = {'name': "Alex", "age": 56}

try:
    print(user["lo"])
except KeyError:
    print("Invalid key")

nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nums)

joined = sum(nums, [])

print(joined)
