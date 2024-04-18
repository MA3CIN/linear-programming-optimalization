import statistics
from statistics import mean

with open('zzz_pareto_individuals_MDR.txt') as f:
    content = f.read().splitlines() 

def get_MDR_from_file(start,end):
    start = start -1
    MDR = []
    for i in range(start,end):   # 3,6 -> 3,4,5
        MDR.append(content[i].split(","))
    return MDR

def dominates(a,b):
    print(a)
    print(b)
    if  a[1] < b[1] or a[2] < b[2] or a[3] < b[3]:
        if a[1] < b[1] and a[2] < b[2] and a[3] < b[3]:
            print(a + " Dominates " + b +  " \n") 
            return True
    print(str(a) + " Does not dominate" + str(b) + " \n")
    return False

# one's MDR score is +1 for each solution from one that is dominated by any solution from two?
def get_mdr_for_two(one,two):
    mdr_score = 0
    for i in range(len(one)):
        for j in range(len(two)):
            if dominates(two[j],one[i]):
                mdr_score += 1
                break
    return mdr_score


# FFGA 
# HLGA  1516-1601, 1603-1689, 1691-1786, 1787-1875, 1877-1983, 1985-2078, 2080-2178, 2180-2272,2273-2356, 2358-2466
# VEGA 3-152, 154-303,305-454, 456-605, 607-756, 758-907, 909-1059, 1060-1209, 1211-1360, 1362-1511
# EW skip for now

# ffga_mdr=[content[4:90].split(",")]
# print(ffga_mdr)
# HLGA_indices=[]
# HLGA = []
# for i in range(10):
#     HLGA.append(get_MDR_from_file(1516,1601))
# VEGA = []
# for i in range(10):
#     VEGA.append(get_MDR_from_file(3,152))

# print('HLGA + \n')
# print(HLGA)

# print('VEGA + \n')
# print(VEGA)

# print(get_mdr_for_two(HLGA,VEGA))

# print(get_mdr_for_two(VEGA,HLGA))

print("huh")
print(dominates(content[1499].split(","),content[1530].split(",")))



# 10 uruchomien, 6 krzyzy:
# FFGA i HLGA
# FFGA i VEGA
# FFGA i EW

# HLGA i VEGA
# HLGA i EW

# VEGA i EW