import sys
import time
from get_text import GetText
from accuracy import Accuracy

def PrintWithSleep(string, sleep_time):
    print(string)
    time.sleep(sleep_time)

orig_text = GetText();

PrintWithSleep("Are you ready?", 1)
PrintWithSleep(orig_text, 0.5)
PrintWithSleep("3", 0.5)
PrintWithSleep("2", 0.5)
PrintWithSleep("1", 0.5)
print("Start")
start_time = time.time()

your_text = ''
c = ''
while(c != '\n'):
    your_text += c
    c = sys.stdin.read(1)

end_time = time.time()

if (orig_text == your_text):
    print("Excellent!")

print("You made", Accuracy(orig_text, your_text), "typos")
print("Your accuracy is: ", 100 * Accuracy(orig_text, your_text) / len(orig_text), "%", sep='')
print("Time spent:", end_time - start_time)

