import statistics
from statistics import mean

with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 


# CZASY JANOS:
# Janos = 39 nodes: Czasy dla kazdej metody + stddev
# Janos = 39 nodes: Average Liczba rozwiazan pareto dla ostatniej gen. + stddev



# UWAGA -> AVERAGE STD_DEV = SQRT (stddev_1^2 + stddev_2^2)/k...   where k is nr of groups

print('JANOS')
print('avg time hlga ' + str(mean([eval(i) for i in content[18:28]])))
print('avg time ffga ' + str(mean([eval(i) for i in content[5:15]])))
print('avg time vega ' + str(mean([eval(i) for i in content[31:41]])))
print('avg time ew ' + str(mean([eval(i) for i in content[44:54]])))

print('JANOS std dev')
print('std dev hlga ' + str(statistics.pstdev([eval(i) for i in content[18:28]])))
print('std dev ffga ' + str(statistics.pstdev([eval(i) for i in content[5:15]])))
print('std dev vega ' + str(statistics.pstdev([eval(i) for i in content[31:41]])))
print('std dev ew ' + str(statistics.pstdev([eval(i) for i in content[44:54]])))


with open('zzz_pareto_czasy.txt') as f:
    content = f.read().splitlines() 

# na 150 mozliwych po selekcji
print('JANOS POS')
print('avg time hlga ' + str(mean([26,28,20,16,11,14,24,29,14,18])))
print('avg time ffga ' + str(mean([85, 74, 82, 72, 77, 66, 71, 70, 68, 73])))
print('avg time vega ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
print('avg time ew ' + str(mean([150,150,150,150,150,150,150,150,150,150])))
#Equal weights jest sus af... bo zaczyna od 150 i do 150. Vega dochodzi do 150 stopniowo


print('JANOS POS std dev')
print('std dev hlga ' + str(statistics.pstdev([26,28,20,16,11,14,24,29,14,18])))
print('std dev ffga ' + str(statistics.pstdev([85, 74, 82, 72, 77, 66, 71, 70, 68, 73])))
print('std dev vega ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))
print('std dev ew ' + str(statistics.pstdev([150,150,150,150,150,150,150,150,150,150])))