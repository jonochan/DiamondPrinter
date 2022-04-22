def drawDiamond(size):
    if size%2 == 0 or size <1:
        return "null"
    lines = size //2
    gap = (size -1)//2
    numStars = 1
    blueprint = ""
    for x in range(lines):
        for y in range(gap):
            blueprint = blueprint + " "
        for z in range(numStars):
            blueprint = blueprint + "*"
        gap = gap - 1
        numStars = numStars + 2
        blueprint = blueprint + "\n"
    for i in range(size):
        blueprint = blueprint + "*"
    numStars = size - 2
    gap = 1
    for x in range(lines):
        blueprint = blueprint + "\n"
        for y in range(gap):
            blueprint = blueprint + " "
        for z in range(numStars):
            blueprint = blueprint + "*"
        gap = gap + 1
        numStars = numStars - 2
    return blueprint

size = int(input("Please enter a positive odd number"))
blueprint = drawDiamond(size)
print(blueprint)
