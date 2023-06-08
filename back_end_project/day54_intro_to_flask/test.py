# # # i want to create a fuction decorator
# # from time import sleep
# # #create a fuction decorator
# # def fuction_decorator(original_function):
# #     def wrapper_function(*arg, **kwrgs):
# #         print("Would you like to be my {}?".format(arg))
# #         sleep(3)
# #         original_function(*arg, **kwrgs)
# #     return wrapper_function
# # #let me have a fuction that print i love you 

# # @fuction_decorator
# # def say_something(name):
# #     print("100 percent yes!!!")

# # @fuction_decorator
# # def say_love():
# #     print("0 percent No!!!")

# # say_something("girlfriend")

# import time
# current_time = time.time()
# print(current_time)

# def speed_calc_decorator(original_function):
#     def wrapper_function():
#         current_time = time.time()
#         original_function()
#         return (time.time() - current_time)
#     return wrapper_function

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
        
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

# print("fast_function run speed: {}".format(fast_function()))
# print("slow_function run speed: {}".format(slow_function()))

# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper_decorator(*args):
        # for number in args:
        #     print(number)
        print(f"{function.__name__}{args} \nIt returned: {function(*args)}")
    return wrapper_decorator


# Use the decorator 👇
@logging_decorator
def multiplication(n1, n2, n3):
    return n1 * n2 * n3

multiplication(1, 2, 3)
