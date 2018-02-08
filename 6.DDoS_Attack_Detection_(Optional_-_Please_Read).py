epoch_intervals = [[123456, 45],[123457, 46],[123458, 1000],[123459, 1129],[123460, 999],[123461, 47],[123462, 50],[123463, 67],[123464,35],[123465, 50],[123466, 10000],[123467, 5000],[123468,60],[123469,60000],[123470,7500],[123471,652560],[123472,60],[123473,6],[123474,600000],[123475,8],[123476,9],[123477,800000],[123478,800000]]

def DDoS(ei):
    # l1 list of interval attacks
    l1 = []
    # l2 intervals of attacks
    l2 = []
    for i in xrange(len(ei)):
        # save interval in l2 when requests exceeds 999
        if ei[i][1] >= 999:
            l2 += [ei[i][0]]
            # when it reaches last element of ei, check if l2 is empty
            if i == len(ei)-1:
                if len(l2) != 0:
                    # if len of l2 is 1 save interval
                    if len(l2) == 1:
                        l1 += [l2]
                        l2 = []
                    # if len of l2 is greater then 1 save first and 
                    # last interval of l2
                    else:
                        l1 += [[l2[0],l2[-1]]]
                        l2 = []
                else:
                    pass
        # when it doesnt exceed 999, check if l2 is empty
        else:
            if len(l2) != 0:
                # if len of l2 is 1 save interval
                if len(l2) == 1:
                    l1 += [l2]
                    l2 = []
                # if len of l2 is greater then 1 save first and 
                # last interval of l2
                else:
                    l1 += [[l2[0],l2[-1]]]
                    l2 = []
            else:
                pass
    return l1
    
print 'DDoS attacks happened in epoch intervals {}'.format(DDoS(epoch_intervals))