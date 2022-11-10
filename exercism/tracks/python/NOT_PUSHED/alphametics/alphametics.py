import itertools

def solve(puzzle):
    letter = sorted(list({i for i in puzzle if str(i).isalpha()}))
    number = list(itertools.permutations(range(10), len(letter)))
    print(letter)
    print(list(number))
    for i in number:
        p: str = puzzle
        for j in range(len(letter)):
            p = p.replace(letter[j], str(i[j]))

        print(p)
        try:
            if eval(p):
                return f"{letter}\n{i}"
        except:
            None


# print(solve("SEND + MORE == MONEY"))
print(solve("TO + GO == OUT"))
# print(solve("""SO+MANY+MORE+MEN+SEEM+TO+SAY+THAT+
#     THEY+MAY+SOON+TRY+TO+STAY+AT+HOME+
#     SO+AS+TO+SEE+OR+HEAR+THE+SAME+ONE+
#     MAN+TRY+TO+MEET+THE+TEAM+ON+THE+
#     MOON+AS+HE+HAS+AT+THE+OTHER+TEN
#     ==TESTS"""))