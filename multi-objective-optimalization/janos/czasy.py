import statistics
from statistics import mean

with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 


# CZASY JANOS:
# Janos = 39 nodes: Czasy dla kazdej metody + stddev
# Janos = 39 nodes: Average Liczba rozwiazan pareto dla ostatniej gen. + stddev



# UWAGA -> AVERAGE STD_DEV = SQRT (stddev_1^2 + stddev_2^2)/k...   where k is nr of groups

print('JANOS')
print('avg time hlga ' + str(mean([eval(i) for i in content[18:25]])))
print('avg time ffga ' + str(mean([eval(i) for i in content[5:15]])))
print('avg time vega ' + str(mean([eval(i) for i in content[31:41]])))
print('avg time ew ' + str(mean([eval(i) for i in content[44:54]])))

print('JANOS std dev')
print('std dev hlga ' + str(statistics.pstdev([eval(i) for i in content[18:25]])))
print('std dev ffga ' + str(statistics.pstdev([eval(i) for i in content[5:15]])))
print('std dev vega ' + str(statistics.pstdev([eval(i) for i in content[31:41]])))
print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[44:54]])))


with open('zzz_pareto_.txt') as f:
    content = f.read().splitlines() 

# # na 150 mozliwych po selekcji
# print('JANOS POS')
# print('avg time hlga ' + str(mean([26,28,20,16,11,14,24,29,14,18])))
# print('avg time ffga ' + str(mean([85, 74, 82, 72, 77, 66, 71, 70, 68, 73])))
# print('avg time vega ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# print('avg time ew ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# #Equal weights jest sus af... bo zaczyna od 150 i do 150. Vega dochodzi do 150 stopniowo


# print('JANOS POS std dev')
# print('std dev hlga ' + str(statistics.pstdev([26,28,20,16,11,14,24,29,14,18])))
# print('std dev ffga ' + str(statistics.pstdev([85, 74, 82, 72, 77, 66, 71, 70, 68, 73])))
# print('std dev vega ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))
# print('std dev ew ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))


def get_gens_from_file(start,end):
    start = start -1
    gens = {}
    for i in range(start,end):   # 3,6 -> 3,4,5
    # dict append to array
        gens[content[i].split(",")[0]] = gens.get(content[i].split(",")[0], [])
        gens[content[i].split(",")[0]].append(content[i].split(",")[2])
    return gens

def biggest_POS_for_dics(my_dict):
    biggest_mean = 0
    gen_nr = 0
    for key in my_dict:
        new_mean = mean([eval(i) for i in my_dict[key]])
        if new_mean > biggest_mean :
            biggest_mean = new_mean
            gen_nr = key
    
    st_dev = statistics.pstdev([eval(i) for i in my_dict[gen_nr]])
    return gen_nr, biggest_mean, st_dev


print('HLGA ') 
print(biggest_POS_for_dics(get_gens_from_file(5243,5956)))
print('FFGA ') 
print(biggest_POS_for_dics(get_gens_from_file(4, 1125)))
print('VEGA ') 
# print(biggest_POS_for_dics(get_gens_from_file(2152, 3171)))
print(str(mean([105,93,78,87,99,78,147,90,147,147])) + ' ' + str(statistics.pstdev([105,93,78,87,99,78,147,90,147,147])))




print('EV ') 
print(str(mean([38,29,25,26,14,23,24,46,41,44])) + ' ' + str(statistics.pstdev([38,29,25,26,14,23,24,46,41,44])))
