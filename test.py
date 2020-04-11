vals = {0: 100, 1: 200, 2: 300, 3: 2000, 4: 1000, 5: 700, 6: 400, 7: 300, 8: 1500, 9: 3000, 10: 4000, 11: 2500, 12: 2000, 13: 500}
for x in range(0, 2**14):
    score = 0
    stri = format(x, "#016b")[2:]
    # print(stri)
    for y in range(14):
        if stri[y] == "1":
            score += vals[y]
    if score == 14200:
        print(stri)