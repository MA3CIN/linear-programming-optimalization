from statistics import mean

with open('zzz_pareto_individuals_MDR.txt') as f:
    content = f.read().splitlines() 

def get_MDR_from_file(start,end):
    start = start -1
    MDR = []
    for i in range(start,end):   # 3,6 -> 3,4,5
        MDR.append(content[i].split(","))
    return MDR


# one's MDR score is +1 for each solution from one that is dominated by any solution from two?
# def get_mdr_for_two(one,two):
#     mdr_score = 0
#     for i in range(len(one)):
#         for j in range(len(two)):
#             if dominates(two[j],one[i]):
#                 mdr_score += 1
#                 break
#     return mdr_score




def get_from_file(start,end):
    start = start -1
    nr_proby = 0
    result = []
    seen = []
    for i in range(start,end):   # 3,6 -> 3,4,5
    # dict append to array
        if content[i][0] == 'O':
            nr_proby += 1
            seen = []
        else:
            if content[i].split(",")[1] not in seen:
                seen.append(content[i].split(",")[1])
                result.append([nr_proby, content[i].split(",")[1], content[i].split(",")[2], content[i].split(",")[3],1])
            else:
                index = get_index_by_value(content[i].split(",")[1], result, nr_proby)
                result[index][4] += 1
    return result

def get_index_by_value(value, array, nr_proby):
    for i in range (0,len(array)):
        if array[i][1] == value and array[i][0] == nr_proby:
            return i

def print_with_nlines(array):
    for i in range(len(array)):
        print(array[i])

# print_with_nlines(get_from_file(4058,4554))

FFGA = get_from_file(4,823)

HLGA = get_from_file(827,1036)

VEGA = get_from_file(1040,2549)

EW = get_from_file(2552,2867)


def dominates(a,b):
    if  a[1] < b[1] or a[2] < b[2] or a[3] < b[3]:
        if a[1] < b[1] and a[2] < b[2] and a[3] < b[3]:
            print(str(a) + " Dominates " + str(b) +  " \n") 
            return True
    print(str(a) + " Does not dominate " + str(b) + " \n")
    return False


# nr_proby, wynik, wynik, wynik, liczebnosc

def get_mdr_for_two(one,two):
    mdr_score = 0
    for i in range(1,11):
        one_stripped = [x for x in one if x[0] == i]
        two_stripped = [x for x in two if x[0] == i]
        for i in range (0, len(one_stripped)):
            for j in range (0, len(two_stripped)):
                if dominates(two_stripped[j],one_stripped[i]):
                    mdr_score += one_stripped[i][4]
                    print("dodaje do zdominowanego!!")
                    break
    return str(mdr_score)


f = open("wyniki_MDR.txt", "a")


f.write("FFGA i HLGA \n")
f.write(get_mdr_for_two(FFGA,HLGA) + "\n")
f.write(get_mdr_for_two(HLGA,FFGA) + "\n")

f.write("FFGA i VEGA \n")
f.write(get_mdr_for_two(FFGA,VEGA) + "\n")
f.write(get_mdr_for_two(VEGA,FFGA) + "\n")

f.write("FFGA i EW \n")
f.write(get_mdr_for_two(FFGA,EW) + "\n")
f.write(get_mdr_for_two(EW,FFGA) + "\n")

f.write("HLGA i VEGA \n")
f.write(get_mdr_for_two(HLGA,VEGA) + "\n")
f.write(get_mdr_for_two(VEGA,HLGA) + "\n")

f.write("HLGA i EW \n")
f.write(get_mdr_for_two(HLGA,EW) + "\n")
f.write(get_mdr_for_two(EW,HLGA) + "\n")

f.write("VEGA i EW \n")
f.write(get_mdr_for_two(VEGA,EW) + "\n")
f.write(get_mdr_for_two(EW,VEGA) + "\n")


f.close()