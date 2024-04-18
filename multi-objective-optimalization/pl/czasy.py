import statistics
from statistics import mean

with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 

print('PL')
print('avg time hlga ' + str(mean([eval(i) for i in content[14:26]])))
print('avg time ffga ' + str(mean([eval(i) for i in content[29:40]])))
print('avg time vega ' + str(mean([eval(i) for i in content[1:11]])))
print('avg time ew ' + str(mean([eval(i) for i in content[43:48]])))

print('PL std dev')
print('std dev hlga ' + str(statistics.pstdev([eval(i) for i in content[14:26]])))
print('std dev ffga ' + str(statistics.pstdev([eval(i) for i in content[29:40]])))
print('std dev vega ' + str(statistics.pstdev([eval(i) for i in content[1:11]])))
print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[43:55]])))


with open('zzz_pareto_.txt') as f:
    content = f.read().splitlines() 

# # na 150 mozliwych po selekcji
# print('POL POS')
# print('avg time hlga ' + str(mean([86, 87, 95, 89, 107, 94 ,99 ,92, 84, 109])))
# print('avg time ffga ' + str(mean([129, 127, 123, 130, 124, 128, 123, 125, 128, 129])))
# print('avg time vega ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# print('avg time ew ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# # #Equal weights jest sus af... bo zaczyna od 150 i do 150. Vega dochodzi do 150 stopniowo


# print('POL POS std dev')
# print('std dev hlga ' + str(statistics.pstdev([86, 87, 95, 89, 107, 94 ,99 ,92, 84, 109])))
# print('std dev ffga ' + str(statistics.pstdev([129, 127, 123, 130, 124, 128, 123, 125, 128, 129])))
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
print(biggest_POS_for_dics(get_gens_from_file(1062,2369)))
print('FFGA ') 
print(biggest_POS_for_dics(get_gens_from_file(2373, 3588)))
print('VEGA ') 
# [150, 138, 150, 138, 138, 18, 150, 81, 150, 150]
print(str(mean([150, 138, 150, 138, 138, 150, 81, 150, 150])) + ' ' + str(statistics.pstdev([150, 138, 150, 138, 138, 150, 81, 150, 150])))
# print(biggest_POS_for_dics(get_gens_from_file(2, 1058)))

print('EV ') 
print(biggest_POS_for_dics(get_gens_from_file(4176, 5496)))