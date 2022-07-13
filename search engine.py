text = input()
word = input()

def search(text,word):
        if word in text:
            return ("Word found")    
        elif word not in text:
            return ("Word not found") 

print(search(text, word)))