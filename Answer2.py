total_second = 9875
hour = total_second // 3600
minute = (total_second % 3600) // 60
second = (total_second % 3600) % 60

print("\n====================================")
print("9875 second = " ,hour, "h", minute, "min", second, "s")
print("Check: ", (hour * 3600) + (minute * 60) + second == total_second)
print("====================================\n")
