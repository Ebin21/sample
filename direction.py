def reduce_dir(directions):

    # Define opposites
    opposite = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST":  "WEST",
        "WEST":  "EAST"
    }
    
    stack = []
    
    for d in directions:
        if stack and opposite[d] == stack[-1]:
          
            # If current direction is opposite
            # to last one in the stack, remove last one
            stack.pop()
        else:
          
            # Otherwise, add current direction to stack
            stack.append(d)
    
    return stack

directions = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"]
res = reduce_dir(directions)
print(res)