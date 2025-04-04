# #1
# def my_func(n):
#     for nums in range(n, -1, -1):
#         yield nums
        
# n = int(input())

# for number in my_func(n):
#     print(number)

# #2
# def squares(a, b):
#     for num in range(a, b + 1):
#         yield num ** 2
# a = int(input())
# b = int(input())

# for square in squares(a, b):
#     print(square)

# #3
# def my_func(n):
#     for nums in range(n + 1):
#         if nums % 3==0 and nums % 4==0:
#             yield nums
            
# n = int(input())
# print(",".join(map(str, my_func(n))))

#4
# def my_fuunc(n):
#     for num in range(n + 1):
#         if num % 2 == 0:
#             yield num
            
# n = int(input())
# print(", ".join(map(str, my_fuunc(n))))
        

# #5
# def my_func(N):
#     for i in range(1, N + 1):
#         yield i ** 2

# N = 5
# gen = my_func(N)

# for square in gen:
#     print(square)