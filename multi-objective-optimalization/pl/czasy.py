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
print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[43:48]])))


with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 

# na 150 mozliwych po selekcji
print('POL POS')
print('avg time hlga ' + str(mean([86, 87, 95, 89, 107, 94 ,99 ,92, 84, 109])))
print('avg time ffga ' + str(mean([129, 127, 123, 130, 124, 128, 123, 125, 128, 129])))
print('avg time vega ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
print('avg time ew ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
# #Equal weights jest sus af... bo zaczyna od 150 i do 150. Vega dochodzi do 150 stopniowo


print('POL POS std dev')
print('std dev hlga ' + str(statistics.pstdev([86, 87, 95, 89, 107, 94 ,99 ,92, 84, 109])))
print('std dev ffga ' + str(statistics.pstdev([129, 127, 123, 130, 124, 128, 123, 125, 128, 129])))
print('std dev vega ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))
print('std dev ew ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))