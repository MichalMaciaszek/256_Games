import math
def isCollision(rect1, rect2):
    # distance = (math.sqrt(math.pow(a_cordinates[0] - b_cordinates[0], 2)) + (math.pow(a_cordinates[1] - b_cordinates[1], 2)))

    collide = rect1.colliderect(rect2)
    return collide
    # if distance < 250:
    #     print(a_cordinates)
    #     print(b_cordinates)
    #     return True
    return False