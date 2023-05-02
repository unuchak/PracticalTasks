class Point2d:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x=0):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y=0):
        self.__y = y

    def __str__(self):
        return f"Point2D: x = {self.__x}, {self.__y}"

