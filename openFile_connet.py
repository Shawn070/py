ftele1=open("TeleAddressBook.txt", "rb")
ftele2=open("EmailAddressBook.txt", "rb")

# ftele1.readline()   # 跳过第一行
# ftele2.readline()
lines1 = ftele1.readlines()
lines2 = ftele2.readlines()

list1_name = []
list1_tele = []
list2_name = []
list2_email = []
lines = []

for line in lines1: # 获取第一个文本中的姓名和电话信息
    elements = line.split()
    list1_name.append(str(elements[0].decode("utf-8")))
    list1_tele.append(str(elements[1].decode("utf-8")))

for line in lines2: # 获取第二个文本中的姓名和邮件信息
    elements = line.split()
    list2_name.append(str(elements[0].decode("utf-8")))
    list2_email.append(str(elements[1].decode("utf-8")))

# 按索引方式遍历姓名列表1
for i in range(len(list1_name)):
    s = ''
    if list1_name[i] in list2_name:
        j = list2_name.index(list1_name[i]) # 找到姓名列表1对应列表2中姓名
        s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
        s += '\n'
    else:
        s = '\t'.join([list1_name[i], list1_tele[i], str("  ------  ")])
        s += '\n'
    lines.append(s)

# 处理姓名列表2中剩余的姓名
for i in range(len(list2_name)):
    s = ''
    if list2_name[i] not in list1_name:
        s = '\t'.join([list2_name[i], str(" ------  "), list2_email[i]])
        s += "\n"
    lines.append(s)
ftele3 = open("AddressBook.txt", "w")
ftele3.writelines(lines)

ftele3.close()
ftele1.close()
ftele2.close()

print("The addressBook are merged!")