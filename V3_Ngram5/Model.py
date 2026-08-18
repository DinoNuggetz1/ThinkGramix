def response():
        scoreboard= {}
        w1 = input("Word 1: ").lower().strip()
        w2 = input("Word 2: ").lower().strip()    
        with open("train.txt", 'r') as file:
          for line in file:
            parts = line.strip().split("-")
            
            if len(parts) == 5:
                file_w1 = parts[0]
                file_w2 = parts[1]
                guess = parts[2]         
                if file_w1 == w1 and file_w2 == w2:
                    if guess not in scoreboard:
                        scoreboard[guess] = 1
                    else:
                        scoreboard[guess] += 1
        for word, score in scoreboard.items():
            print(f"Word: {word} | Weight: {score}")
response()
