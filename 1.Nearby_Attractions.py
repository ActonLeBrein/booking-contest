from math import *
import operator

N = int(raw_input())
attractions = {}
for _ in xrange(N):
    l = raw_input().split()
    attractions[int(l[0])] = [float(l[1]),float(l[2])]

M = int(raw_input())
users = []
for _ in xrange(M):
    l = raw_input().split()
    l[0] = float(l[0])
    l[1] = float(l[1])
    l[3] = int(l[3])
    users.append(l)

def distance_attraction( lat_org, long_org, lat_dest, long_dest ):
    return acos( sin( radians(lat_org) ) * sin( radians(lat_dest) ) + cos( radians(lat_org) ) * cos( radians(lat_dest) ) * cos( radians(long_dest) - radians(long_org) ) ) * 6371.0

def time_attraction( distance, transport ):
    if transport == 'metro':
        return distance / 20.0 * 60.0
    elif transport == 'bike':
        return distance / 15.0 * 60.0
    elif transport == 'foot':
        return distance / 5.0 * 60.0
    else:
        return 0

def min_dic( dic ):
    minimums = []
    minimum = float('inf')
    for k in dic.keys():
        if dic[k] < minimum:
            minimum = dic[k]
            minimums = [k]
        elif dic[k] == minimum:
            minimums += [k]
        else:
            pass
    return sorted(minimums)
    
def reachable_attractions( attractions, user ):
    reachables = {}
    for ID in attractions.keys():
        time = time_attraction( round(distance_attraction( user[0], user[1], attractions[ID][0], attractions[ID][1] ),2), user[2] )
        if time <= user[3]:
            reachables[ID] = time
    IDs = []
    while len(reachables) > 0:
        ID = min_dic(reachables)
        for i in ID:
            reachables.pop(i)
        IDs += ID
    return IDs

for user in users:
    reachables = reachable_attractions( attractions, user )
    print ' '.join( map( str, reachables) )