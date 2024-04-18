import statistics
from statistics import mean

with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 

print('PL')
print('avg time hlga ' + str(mean([eval(i) for i in content[15:23]])))
print('avg time ffga ' + str(mean([eval(i) for i in content[25:30]])))
print('avg time vega ' + str(mean([eval(i) for i in content[33:38]])))
print('avg time ew ' + str(mean([eval(i) for i in content[3:12]])))

print('PL std dev')
print('std dev hlga ' + str(statistics.pstdev([eval(i) for i in content[15:23]])))
print('std dev ffga ' + str(statistics.pstdev([eval(i) for i in content[25:30]])))
print('std dev vega ' + str(statistics.pstdev([eval(i) for i in content[33:38]])))
print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[3:12]])))


with open('zzz_pareto_.txt') as f:
    content = f.read().splitlines() 

# na 150 mozliwych po selekcji
print('POL POS')
print('avg time hlga ' + str(mean([144, 140, 116, 28, 130, 12, 150, 57])))
print('avg time ffga ' + str(mean([122, 115, 117, 136, 111])))
print('avg time vega ' + str(mean([131, 125, 135, 131, 124])))
print('avg time ew ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# #Equal weights jest sus af... bo zaczyna od 150 i do 150. Vega dochodzi do 150 stopniowo


print('POL POS std dev')
print('std dev hlga ' + str(statistics.pstdev([144, 140, 116, 28, 130, 12, 150, 57])))
print('std dev ffga ' + str(statistics.pstdev([122, 115, 117, 136, 111])))
print('std dev vega ' + str(statistics.pstdev([131, 125, 135, 131, 124])))
print('std dev ew ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))