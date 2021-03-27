import westjr
jr = westjr.WestJR()

trains = jr.trains(line="kobesanyo")

for i in range(len(trains)):
    print("{} {} {}行は".format(trains[i].no, trains[i].displayType, trains[i].dest_text), end="")
    print("現在{}分遅れで".format(trains[i].delayMinutes), end="")
    if trains[i].next:  # 停車中の場合，次駅はNone
        print("{}駅-{}駅間を走行中".format(trains[i].prev, trains[i].next))
    else:
        print("{}駅に停車中".format(trains[i].prev))
