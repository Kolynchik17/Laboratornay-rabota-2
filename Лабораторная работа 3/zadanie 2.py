# TODO Напишите функцию find_common_participants
def find_common_participants(x,y):
    sp=[]
    a=x.split("|")
    b=y.split("|")
    for i in range(0,len(a)):
        for g in range (0,len(b)):
            if (a[i]==b[g]):
                sp.append(a[i])
    sp.sort()
    return sp

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
prov=find_common_participants(participants_first_group,participants_second_group)
print(prov)
# TODO Провеьте работу функции с разделителем отличным от запятой
