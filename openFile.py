infile = open("data_test.txt", "r")
for i in range(5):
    line = infile.readline()
    # line = infile.readlines()
    print(line[:-1])
    # print(line)		# 输出行间空一行