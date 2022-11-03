import datetime

start_time = datetime.datetime.now()

sum = 0
for num in range(100000):
    sum = sum + num

sum_time = datetime.datetime.now()
print("合計値" + str(sum))

sum2 = 0
for num2 in range(100000):
    sum2 = sum2 + num2

sum_time_2 = datetime.datetime.now()
print("合計値2" + str(sum))

rap_time_sum1 = sum_time - start_time
rap_time_sum2 = sum_time_2 - sum_time
total_time = sum_time_2 - start_time

print("time(sum1)" + str(rap_time_sum1))
print("time(sum2)" + str(rap_time_sum2))
print("time(total)" + str(total_time))