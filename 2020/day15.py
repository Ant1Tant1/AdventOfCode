
data = [13,16,0,12,15,1]

first_last_spoken = {}
second_last_spoken = {}

# turn
turn = 1
# initialization
while turn < len(data) + 1:
    first_last_spoken[data[turn - 1]] = turn
    turn += 1


last_turn = 30000000
last_spoken = data[-1]
zero = 0
# main loop
while turn <= last_turn:
    # get next_spoken depending of it actually exist in second last spoken
    next_spoken = first_last_spoken[last_spoken] - second_last_spoken[last_spoken] if last_spoken in second_last_spoken else zero
    
    # if next_spoken already exist in firts, pass it to second
    if next_spoken in first_last_spoken:
        second_last_spoken[next_spoken] = first_last_spoken[next_spoken]
    # save it in first last spoken anyways
    first_last_spoken[next_spoken] = turn
    
    # get it, and increment
    last_spoken = next_spoken
    turn += 1

print("Pb 1:", last_spoken)

    