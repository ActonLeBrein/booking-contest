cities = {}
S = int(raw_input())

while True:
    try:
        a = raw_input()
        a = a.split(':')
        cities[a[0]] = a[1].split(',')
    except EOFError:
        break

M = []
for ci in cities.keys():
    N = []
    for cj in cities.keys():
        if ci == cj:
            N += [set([])]
        else:
            N += [set(cities[ci]).intersection(cities[cj])]
    M += [N]

M1 = []
l = 0
for r in M:
    TL = [0]*l
    M1 += [TL+[len(k) for k in r[l:]]]
    l += 1
    
M2 = [item for sublist in M1 for item in sublist]

def max_matrix(m):
    return [m.index(max(m))/len(M1[0]), m.index(max(m))%len(M1[0])]

def zero_group(N,p):
    G = [i for i, j in enumerate(M2) if j == N]
    for i in G:
        pos = [i/len(M[0]), i%len(M[0])]
        if M[pos[0]][pos[1]] == M[p[0]][p[1]]:
            M2[i] = 0

def tag_group(N,p):
    tags = M[p[0]][p[1]]
    cities_match = []
    for k in cities.keys():
        if tags.issubset(set(cities[k])):
            cities_match.append(k)
    return [sorted(cities_match),sorted(list(tags))]

def make_groups():
    maxi = max(M2)
    current_maxi = maxi
    groups_cities = []
    while maxi >= S:
        groups_N_cities = []
        while current_maxi == maxi:
            groups_N_cities.append(tag_group(maxi,max_matrix(M2)))
            zero_group(maxi,max_matrix(M2))
            maxi = max(M2)
        current_maxi = maxi
        groups_cities += sorted(groups_N_cities)
    return groups_cities

for x in make_groups():
    print ','.join(x[0])+':'+','.join(x[1])