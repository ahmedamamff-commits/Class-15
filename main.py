#take user input
a = input("Enter a word:")
#program to check break keyword
for i in a:
    if (i == "A"): #condition 1
        print("A is found")
        break #break statement
    else:
        #display the result
        print("A is not found")