#!/usr/bin/python
import sys
from random import sample
names=[]
games=[]

def season_schedule_order(games):
    schedule = []
    last_pair = []
    timer = 0
    while games:
        r_pair = sample(games,1)[0]
        rev_pair = [r_pair[1],r_pair[0]]
        if r_pair[0] in last_pair or r_pair[1] in last_pair:
            timer += 1
            if timer < 20:
                continue
            else:
                break
        if r_pair in games:
            games.remove(r_pair)
        elif rev_pair in games:
            games.remove(rev_pair)
        else:
            continue
        last_pair = r_pair
        #yield r_pair
        schedule.append(r_pair)
    #print "timer:",timer
    #print "r_pair:",r_pair
    #print "last_pair:",last_pair
    return schedule

try:
    #input_count=sys.stdin.readline()
    input_count=raw_input("No. of players/teams:")
    count=int(input_count)
    tries = 100
    print "Players:"
    for player in range(count):
        player=sys.stdin.readline()
        names.append(player.rstrip())

    games = [[names[i],names[j]] for i in range(count) for j in range(i+1,count)]
    total_games = len(games)
    org_games = games[:]
    opt_schedule = False

    for i in range(tries):
        games = org_games[:]
        #print "Games:",games
        schedule = season_schedule_order(games)
        #print schedule

        if len(schedule) == total_games:
        #for (player1, player2) in season_schedule_order(games):
            print "Optimized Schedule:"
            for (player1, player2)  in schedule:
                print "%s\t%s"%(player1,player2)
            opt_schedule = True
            break
    if not opt_schedule:
        print "Optimized schedule not generated. Try again."
except Exception, e:
    print str(e)
