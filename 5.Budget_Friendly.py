N,B = map(int,(raw_input().split(' ')))

C = []

for _ in xrange(N):
    hotels = []
    H = int(raw_input())
    for _ in xrange(H):
        P,S = raw_input().split(' ')
        hotels.append([int(P),float(S)])
    C.append(hotels)
#print cities

MSCORE = 0

def itinerary( cities, score, budget ):
    global MSCORE
    if not cities:
        if score > MSCORE:
            MSCORE = score
        return
    for h in cities[0]:
        a = budget + h[0]
        if a <= B:
            itinerary( cities[1:], score + h[1], a )
    
itinerary( C, 0, 0 )
print round( MSCORE, 2 ) if MSCORE != 0 else -1