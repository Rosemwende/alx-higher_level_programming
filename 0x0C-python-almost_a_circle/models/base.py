#!/usr/bin/python3
"""Write the first class Base"""
class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)  # Dummy instance
        elif cls.__name__ == "Square":
            obj = cls(1)  # Dummy instance
        obj.update(**dictionary)
        return obj

    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                json_list = cls.from_json_string(json_str)
                return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes list_objs to CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes CSV file to list of instances """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

       def draw(list_rectangles, list_squares):
        """ Opens a window and draws all Rectangles and Squares """
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()
        pen.hideturtle()

        for rect in list_rectangles:
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.setheading(0)
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.penup()

        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.setheading(0)
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.penup()

        screen.mainloop()
