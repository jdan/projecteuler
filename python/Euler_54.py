#!/usr/bin/python

import urllib

def decode(s):
    h = s[0]
    h = int(h.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14'))
    s = s[1]
    
    return [h, s]
    
def quicksort(hand):
    if len(hand) <= 1:
        return hand
        
    pivot = hand[0]
    less_than = []
    greater_than = []
    
    for card in hand[1:]:
        if card[0] > pivot[0]:
            greater_than.append(card)
        else:
            less_than.append(card)
            
    return quicksort(less_than) + [pivot] + quicksort(greater_than)
    
def run(hand):
    r = []
    last = hand[0]
    
    for card in hand[1:]:
        r.append(card[0] - last[0])
        last = card
        
    return r
    
def flush(hand):
    return hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]
    
types = {0 : 'royal flush',
         1 : 'straight flush',
         2 : 'four of a kind',
         3 : 'full house',
         4 : 'flush',
         5 : 'straight',
         6 : 'three of a kind',
         7 : 'two pair',
         8 : 'pair',
         9 : 'high card'}
         
def high_pair(hand):
    collate = []
    for card in hand:
        collate.append(card[0])
        
    m = 0
    for i in range(2, 15):
        if collate.count(i) > 1:
            if i > m:
                m = i
                
    return m
    
def t_score(hand):
    r = run(hand)
    
    if r == [1, 1, 1, 1] and flush(hand):
        if hand[0][0] == 10:
            return 0
        else:
            return 1
    elif r[:3] == [0, 0, 0] or r[1:] == [0, 0, 0]:
        return 2
    elif (r[:2] == [0, 0] and r[3] == 0) or (r[2:] == [0, 0] and r[0] == 0):
        return 3
    elif flush(hand):
        return 4
    elif r == [1, 1, 1, 1]:
        return 5
    elif r[:2] == [0,0] or r[1:3] == [0,0] or r[2:] == [0,0]:
        return 6
    elif r.count(0) == 2:
        return 7
    elif r.count(0) == 1:
        return 8
    else:
        return 9
        
def score(hand):
    s1 = t_score(hand)
    
    hand_t = []
    # replace all the aces with value 1
    for i, v in enumerate(hand):
        c = [0, 0]
        if v[0] == 14:
            c[0] = 1
        else:
            c[0] = v[0]
        
        c[1] = v[1]
        hand_t.append(c)
            
    hand_t = quicksort(hand_t)
    s2 = t_score(hand_t)
    
    return min(s1, s2)

def e54():
    player1_wins = 0
    for line in urllib.urlopen('http://projecteuler.net/project/poker.txt').readlines():
        store = player1_wins
        
        p1_hand = quicksort(map(decode, line.split()[:5]))
        p2_hand = quicksort(map(decode, line.split()[5:]))
        
        p1_s = score(p1_hand)
        p2_s = score(p2_hand)
        
        if p1_s < p2_s:
            player1_wins += 1
        elif p1_s > p2_s:
            continue
        elif p1_s in [3, 6, 7, 8]:
            if high_pair(p1_hand) > high_pair(p2_hand):
                player1_wins += 1
            elif high_pair(p1_hand) < high_pair(p2_hand):
                continue
            else:
                for i in range(4, -1, -1):
                    if p1_hand[i][0] > p2_hand[i][0]:
                        player1_wins += 1
                        break
                    elif p1_hand[i][0] < p2_hand[i][0]:
                        break
                    else:
                        pass
        else:
            for i in range(4, -1, -1):
                if p1_hand[i][0] > p2_hand[i][0]:
                    player1_wins += 1
                    break
                elif p1_hand[i][0] < p2_hand[i][0]:
                    break
                else:
                    pass
                    
    print 'Total: %s' % (player1_wins)
        
if __name__ == '__main__':
    e54()