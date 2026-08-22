import random
import time
passages = ["""The moon looks bright because it reflects sunlight.
Its surface is covered with countless craters and mountains.""",

"""The ocean is home to millions of fascinating creatures.
Some deep-sea animals can even produce their own light.""",

"""Honey can remain edible for thousands of years.
Its natural properties make it difficult for bacteria to grow.""",

"""A rainbow appears when sunlight passes through water droplets.
The light bends and separates into different colors.""",

"""Mountains are formed over millions of years.
Some are still slowly changing because of Earth's movements."""]
print("="*70)
print("Welcome to the Typing Speed Test!")
print("="*70)
def start_test():
    print("\nyou will be given a passage to typen." "\nType it as accurately and quickly as you can.")
    print("\nWhen your are ready,Press Enter to start the test.")
    input()
    passage = random.choice(passages)
    print(passage)
    start_time = time.time()
    user_input = input("\nType the passage above:\n")
    end_time = time.time()
    wpm,time_taken = calculate_wpm(user_input,start_time,end_time)
    show_results(wpm,time_taken)
    acc = accuracy(user_input,passage)
    print(f"Your typing accuracy is: {acc:.2f}%")
def calculate_wpm(user_input,start_time,end_time):
    words = user_input.split()
    time_taken = end_time - start_time
    wpm = len(words) / time_taken * 60
    return wpm,time_taken
def show_results(wpm,time_taken):
    print("\nTest completed!")
    print("<","-"*10,">")
    print(" RESULTS")
    print("<","-"*10,">")
    print(f"Your typing speed is:{wpm:.2f} words per minute.")
    print(f"Time taken: {time_taken:.2f} seconds.")
def accuracy(user_input,passage):
    typed_words = user_input.split()
    correct_words = passage.split()
    count = 0
    for typed_word, correct_word in zip(typed_words, correct_words):
        if typed_word == correct_word:
            count += 1
    accuracy = (count / len(correct_words)) * 100
    return accuracy
start_test()