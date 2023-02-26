'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

'''

#Write your code below this line 👇
def paint_calc(height,width,cover):
    no_of_cans = (height*width)/cover
    no_of_cans = round(no_of_cans)
    print(f"You'll need {no_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)