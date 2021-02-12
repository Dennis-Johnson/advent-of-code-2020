
#seq = [0, 3, 6]
seq = [1,0,16,5,17,4]

history = {} # holds key-value pairs of {number: turn}
turn = 1

for num in seq:
    history[num] = turn
    turn += 1

recent = seq[-1]

while turn <= 30000000:
    lastTurn = history.get(recent, -1)
    history[recent] = turn - 1  

    if lastTurn == -1:
        next_ = 0
    else:
        next_ = turn - 1 - lastTurn

    recent = next_
    print("Turn: {} --- Recent {} --- Next {}".format(turn, recent, next_))
    turn += 1

print (recent)
