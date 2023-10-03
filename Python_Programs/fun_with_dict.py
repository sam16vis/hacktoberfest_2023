# Word Counter in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}

for word in words:
    word = word.lower().strip(",.!?")
    word_count[word] = word_count.get(word, 0) + 1
    
print("Word Count:", word_count)


# --------------------------------------------------------------------------------------------------------------------
# Dictionary-based Quiz

quiz = {
    'Who is the author of "Harry Potter"?': 'jk rowling',
    'What is the capital of France?': 'paris',
    'Which planet is known as the Red Planet?': 'mars',
}

score = 0
for question, answer in quiz.items():
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answer)

print("Your total score is:", score)


# --------------------------------------------------------------------------------------------------------------------
#Reverse Key-Value Lookup

def reverse_lookup(d):
    return {v: k for k, v in d.items()}

sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print("Original Dictionary:", sample_dict)
print("Reversed Dictionary:", reverse_lookup(sample_dict))





