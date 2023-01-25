with open('sentiment_values.csv') as f:
    text = f.read()
lines = text.split("\n")
data = {}

for i in range(len(lines)):
    theline = lines[i].split(",")
    data[ theline[0]] = float(theline[1])

word = input("Please enter a word: ")
print(data[word])





