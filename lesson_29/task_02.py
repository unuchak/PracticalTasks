from manager import Manager
from point2d import Point2d

p1 = Point2d()
p2 = Point2d(3, 4)

print(p1)
print(p2)

man = Manager()

distance = man.calculate_distance(p2, p1)
print(f"Distance between points is {distance}.")
