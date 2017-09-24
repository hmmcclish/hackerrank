S = raw_input().strip()
split_S = [S[start:start+3] for start in range(0, len(S), 3)]
counter = 0
for x in range(len(split_S)):
    if split_S[x][0] != "S" and split_S[x][0] != "s":
        counter += 1
    if split_S[x][1] != "O" and split_S[x][1] != "o":
        counter += 1
    if split_S[x][2] != "S" and split_S[x][2] != "s":
        counter += 1
print counter
