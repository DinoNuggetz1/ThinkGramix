import string
def training():
        with open("dataset1.txt", 'r') as d:
            for line in d:
                data = line.strip(string.punctuation).lower().split()
                for i in range(len(data)-4):
                    cword = data[i].strip(string.punctuation)
                    word = data[i + 1].strip(string.punctuation)
                    word2 = data[i + 2].strip(string.punctuation)
                    word3 = data[i + 3].strip(string.punctuation)
                    word4 = data[i + 4].strip(string.punctuation)
                    if cword.isdigit() or word.isdigit() or word2.isdigit():
                        continue 
                    if cword.isalpha() and word.isalpha() and word2.isalpha():
                        pair = cword + "-" + word + '-' + word2 + '-' + word3 + '-' + word4
                        res = open("train.txt", 'a')
                        res.write(pair + "\n")
        with open("dataset2.txt", 'r') as d:
                    for line in d:
                        data = line.strip(string.punctuation).lower().split()
                        for i in range(len(data)-4):
                            cword = data[i].strip(string.punctuation)
                            word = data[i + 1].strip(string.punctuation)
                            word2 = data[i + 2].strip(string.punctuation)
                            word3 = data[i + 3].strip(string.punctuation)
                            word4 = data[i + 4].strip(string.punctuation)
                            if cword.isdigit() or word.isdigit() or word2.isdigit():
                                continue 
                            if cword.isalpha() and word.isalpha() and word2.isalpha():
                                pair = cword + "-" + word + '-' + word2 + '-' + word3 + '-' + word4
                                res = open("train.txt", 'a')
                                res.write(pair + "\n")
