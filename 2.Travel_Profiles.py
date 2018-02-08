N = int(raw_input())
hotels = {}
for _ in xrange(N):
    l = raw_input().split()
    hotels[int(l[0])] = [int(l[1]),l[2:]]

M = int(raw_input())
users = []
for _ in xrange(M):
    l = raw_input().split()
    l[0] = int(l[0])
    users.append(l)

def checks_requeriments(user,hotel):
    return (set([user[1]]).issubset(hotel[1])) and user[0] >= hotel[0]

def sort_hotels_facilities(IDs,user,hotels):
    F = [len(hotels[k][1]) for k in IDs]
    R = []
    while len(IDs) > len(R):
        IN_F = [i for i, j in enumerate(F) if j == max(F)]
        ID_F = [IDs[k] for k in IN_F]
        P = [hotels[m][0] for m in ID_F]
        Q = []
        while len(ID_F) > len(Q):
            IN_P = [i for i, j in enumerate(P) if j == min(P)]
            ID_P = sorted([ID_F[k] for k in IN_P])
            for i in IN_P:
                P[i] = float('inf')
            Q += ID_P
        for i in IN_F:
            F[i] = 0
        R += Q
    return R
print hotels
print users
for user in users:
    IDs = []
    for hotel in hotels.keys():
        if checks_requeriments(user,hotels[hotel]):
            IDs.append(hotel)
    ans = sort_hotels_facilities(IDs,user,hotels)
    print ' '.join(map(str,ans))