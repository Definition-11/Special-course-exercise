text = "It's terrible how my dog thinks every knock on the door is for him - he must think he's the most popular guy in the neighborhood! It's also terrible how he can sleep all day and yet, the minute I try to take a nap, he decides it's playtime. The terrible thing is, no matter how many times I explain it to him, he still doesn't understand the concept of 'personal space.' It's terrible how he can find the one spot of mud in an entire field and roll in it. And it's even more terrible how he can smell food from a mile away, yet can't find the toy I just threw for him. It's terrible how he can hear a wrapper from three rooms away, but suddenly goes deaf when I call his name. The most terrible thing of all is how, despite all these quirks, he's still the most terrible companion I could ask for. It's simply terrible!"
import re
char = "terrible"
count = len(re.findall(char, text))
print(count)

new_text = text.replace("terrible", " marvellous" * int(count % 2) + " pathetic" * (
    int(count / 2)) if count > 0 else "")

with open("result.txt", "w") as file:
    file.write(new_text)