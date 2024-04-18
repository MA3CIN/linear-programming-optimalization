import statistics
from statistics import mean

with open('zzz_pareto_individuals_MDR.txt') as f:
    content = f.read().splitlines() 


# pojedynczy wynik dla ostatniej generacji
print (content[7].split(","))
# print([eval(i) for i in content[18:28]])

# FFGA 4,90,165,248,321,399,466,538,609,678,752
# HLGA

ffga_mdr=[content[4:90].split(",")]
print(ffga_mdr)

def dominates(a,b):
    if  a[1] < b[1] or a[2] < b[2] or a[3] < b[3]:
        if a[1] < b[1] and a[2] < b[2] and a[3] < b[3]:
            return True
    else:
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


# 10 uruchomien, 6 krzyzy:
# FFGA i HLGA
# FFGA i VEGA
# FFGA i EW

# HLGA i VEGA
# HLGA i EW

# VEGA i EW

#ale to moze lepiej dla PL sieci jak zwerfyikowane wyniki bd, idk


# print('JANOS')
# print('avg time hlga ' + str(mean([eval(i) for i in content[18:28]])))
# print('avg time ffga ' + str(mean([eval(i) for i in content[5:15]])))
# print('avg time vega ' + str(mean([eval(i) for i in content[31:41]])))
# print('avg time ew ' + str(mean([eval(i) for i in content[44:54]])))

# print('JANOS std dev')
# print('std dev hlga ' + str(statistics.pstdev([eval(i) for i in content[18:28]])))
# print('std dev ffga ' + str(statistics.pstdev([eval(i) for i in content[5:15]])))
# print('std dev vega ' + str(statistics.pstdev([eval(i) for i in content[31:41]])))
# print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[44:54]])))


