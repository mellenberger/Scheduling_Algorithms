import random
import numpy as np

def CVB_ETC_1(t, m, vtask, vmach, utask, file_name, consistency):
    # Low task / low machine; high task / low machine; high task / high machine;
    file1 = open(file_name,'w')
    # Coefficient of Variation ETC Matrix
    atask = 1 / (vtask ** 2)
    amach = 1 / (vmach ** 2)
    btask = utask / atask
    q = []
    bmach = []
    e = [[0 for x in range(m)] for y in range(t)]
    for i in range(t):
        q.append(random.gammavariate(atask, btask))
        bmach.append(q[i] / amach)
        for j in range(m):
            e[i][j] = round(random.gammavariate(amach, bmach[i]))
    
            
    # Add deadlines for each task
    d = np.zeros((t,1))
    for i in range(t):
        d[i] = random.randrange(min(e[i]), max(e[i]))
    e = np.hstack((e,d))


    if consistency == 'consistent':
        #Consistent
        for i in range(t):
            print(*sorted(e[i]), file = file1)

    elif consistency == 'partiallyconsistent':
        #PartiallyConsistent
        for i in range(t):
            even = []
            odd = []
            New_list = []
            for x in range(len(e[i])):
                if x % 2 == 0:
                    even.append(e[i][x])
                else:
                    odd.append(e[i][x])
            even = sorted(even)
            num1 = 0
            num2 = 0
            for x in range(len(e[i])):
                if x % 2 == 0:
                    New_list.append(even[num1])
                    num1 += 1
                else:
                    New_list.append(odd[num2])
                    num2 += 1
            print(*New_list, file = file1)

    else:
        #Inconsistent
        for i in range(t):
            print(*e[i], file = file1)

    file1.close()


def CVB_ETC_2(t,m,vtask,vmach, umach, file_name, consistency):
    file1 = open(file_name,'w')
    # Coefficient of Variation ETC matrix
    # Low task heterogeneity high machine heterogeneity
    atask = 1 / (vtask**2)
    amach = 1 / (vmach**2)
    bmach = umach / amach
    p = []
    btask = []
    e = [[0 for x in range(m)] for y in range(t)]
    for j in range (m):
        p.append(random.gammavariate(amach,bmach))
        btask.append(p[j] / atask)
        for i in range (t):
            e[i][j] = round(random.gammavariate(atask,btask[j]))
 
    # Add deadlines for each task
    d = np.zeros((t,1))
    for i in range(t):
        d[i] = random.randrange(min(e[i]), max(e[i]))
    e = np.hstack((e,d))

    if consistency == 'consistent':
        #Consistent
        for i in range(t):
            print(*sorted(e[i]), file = file1)
        file1.close()

    elif consistency == 'partiallyconsistent':
        #PartiallyConsistent
        for i in range(t):
            even = []
            odd = []
            New_list = []
            for x in range(len(e[i])):
                if x % 2 == 0:
                    even.append(e[i][x])
                else:
                    odd.append(e[i][x])
            even = sorted(even)
            num1 = 0
            num2 = 0
            for x in range(len(e[i])):
                if x % 2 == 0:
                    New_list.append(even[num1])
                    num1 += 1
                else:
                    New_list.append(odd[num2])
                    num2 += 1
            print(*New_list, file = file1)
        file1.close()   
        
    else:
        #Inconsistent
        for i in range(t):
            print(*e[i], file = file1)
        file1.close()