import random,time

#Get  a sequence length from the user
digits = input('How many digits do you want to guess:')
digits = int(digits)

#Create a random sequence
sequence = []
for i in range(0,digits):
    sequence.append(random.randint(0,9))
print(sequence)

#Show it for 5 seconds
time.sleep(5)
#Hide the sequence
for i in range(0,50):
    print("")
#Check if the user can recall the sequence
for i in range (0,digits):
    print('enter number at index' +str(i))
    num = int(input())
    if num == sequence[i]:
        print('correct')
    else:
        print('Wrong')
        break
    sequence.append(random.randint(0,9))
print(sequence)
