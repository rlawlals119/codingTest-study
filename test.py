# print("         ,r\'\"7\nr`-_   ,\'  ,/\n \. \". L_r\'\n   `~\/\n      |\n      |\n")

# s = input()
# i = int(input())

# print(s[i - 1:i])

# nums = list(map(int, input().split()))
# # 1 ~ 8 or 8 ~ 1
# flag = False
# if nums[0] == 1:
#     for i in range(0, len(nums) - 1):
#         if nums[i] + 1 != nums[i + 1]:
#             print('mixed')
#             flag = True
#             break
#     if not flag:
#         print('ascending')

# elif nums[0] == 8:
#     for i in range(0, len(nums) - 1):
#         if nums[i] - 1 != nums[i + 1]:
#             print('mixed')
#             flag = True
#             break
#     if not flag:
#         print('descending')

# else:
#     print('mixed')

a = input()
b = input()
c = input()

print(int(a) + int(b) - int(c))
print(int(a + b) - int(c))