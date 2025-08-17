

def word_count(text):
    words = text.split()
    return len(words)

# Take input from user
text = input("Enter a sentence or paragraph: ")

print("Total words:", word_count(text))
