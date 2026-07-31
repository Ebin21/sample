# Program to print a 5-pointed star shape
for row in range(12):
    for col in range(21):
        # Logic for the top triangle tip
        top_tip = (row < 4 and (col == 10 - row or col == 10 + row))
        
        # Logic for the horizontal crossbar
        crossbar = (row == 4 and (col <= 6 or col >= 14))
        
        # Logic for the wide upper-side wings
        wings = (row > 4 and row < 7 and (col == row + 2 or col == 18 - row))
        
        # Logic for the inner lower legs
        legs = (row >= 7 and (col == 14 - row or col == 6 + row))
        
        # Print a star if any condition is met, otherwise print a space
        if top_tip or crossbar or wings or legs:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line
