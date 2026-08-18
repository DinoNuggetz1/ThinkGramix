rdata = input(": ").lower()
pdata = str(rdata)
glen = 1000
brain = {}
with open("/usr/share/dict/words", "r") as file:
    for line in file:

        word = line.strip().lower()

        if word.startswith(rdata):
            clen = len(word)
            if clen < glen or (clen == glen ):
                glen = clen
                bm = word
                print(bm)
