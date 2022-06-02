cnt_list = list()
for i in range(6, 127):
  cnt = 0
  # print("i",i)
  binary = bin(i)
  # print("binary", binary)
  for x in binary:
    if x == "1":
      cnt += 1
  if cnt == 6:
    print(i)
  cnt_list.append(cnt)
  # print("cnt",cnt)

# print(max(cnt_list))