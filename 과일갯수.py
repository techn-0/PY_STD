fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def count_fruits(target):
    num = 0
    for i in fruits:
        if i == '사과':
            num += 1
    return num

subak_count = count_fruits('수박')
print(subak_count)

gam_count = count_fruits('감')
print(gam_count)