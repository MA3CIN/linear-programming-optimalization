import statistics
from statistics import mean

with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 

# print('PL')
# print('avg time hlga ' + str(mean([eval(i) for i in content[15:23]])))
# print('avg time ffga ' + str(mean([eval(i) for i in content[25:30]])))
# print('avg time vega ' + str(mean([eval(i) for i in content[33:38]])))
# print('avg time ew ' + str(mean([eval(i) for i in content[3:9]])))

# print('PL std dev')
# print('std dev hlga ' + str(statistics.pstdev([eval(i) for i in content[15:23]])))
# print('std dev ffga ' + str(statistics.pstdev([eval(i) for i in content[25:30]])))
# print('std dev vega ' + str(statistics.pstdev([eval(i) for i in content[33:38]])))
# print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[3:9]])))


with open('zzz_pareto_.txt') as f:
    content = f.read().splitlines() 

# na 150 mozliwych po selekcji
# print('POL POS')
# print('avg time hlga ' + str(mean([144, 140, 116, 28, 130, 12, 150, 57])))
# print('avg time ffga ' + str(mean([122, 115, 117, 136, 111])))
# print('avg time vega ' + str(mean([131, 125, 135, 131, 124])))
# print('avg time ew ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# # #Equal weights jest sus af... bo zaczyna od 150 i do 150. Vega dochodzi do 150 stopniowo


# print('POL POS std dev')
# print('std dev hlga ' + str(statistics.pstdev([144, 140, 116, 28, 130, 12, 150, 57])))
# print('std dev ffga ' + str(statistics.pstdev([122, 115, 117, 136, 111])))
# print('std dev vega ' + str(statistics.pstdev([131, 125, 135, 131, 124])))
# print('std dev ew ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))


# NOWY POS -> z 10 uruchomien srednia wartosc POS dla kazdej generacji (150 srednich wartosci) i bierzemy z tego maks!
# FFGA - get start line, go until empty line

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


#HLGA
# print(get_gens_from_file(1106,1921))
print('HLGA ') 
print(biggest_POS_for_dics(get_gens_from_file(1106,1921)))
print('FFGA ') 
print(biggest_POS_for_dics(get_gens_from_file(1942, 2433)))
print('VEGA ') 
print(biggest_POS_for_dics(get_gens_from_file(2437, 3009)))

print('EV ') 
# print(biggest_POS_for_dics(get_gens_from_file(2437, 3009)))
print(str(mean([12,34,25,30,24,29])) + ' ' + str(statistics.pstdev([12,34,25,30,24,29])))



# generacje hlga 69, ffga 95, vega 90 ew..?

# print("Weryfikacja")
# print(statistics.pstdev([13,15,18,12,11,21,19,]))