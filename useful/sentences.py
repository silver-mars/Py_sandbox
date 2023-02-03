sentences = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
def process(sentences):
    result = []
    final = []
    for element in sentences:
        result = [word for word in element.split() if word.isalpha()]
        final.append(' '.join(result))
    return final

print(process(sentences))
