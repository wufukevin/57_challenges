class PizzaParty(object):
    def ask_for_function(self):
        self.function = input("Select Pizza Party Function: Cut Or Count")
        if self.function.lower() != 'cut' and self.function.lower() != 'count':
            raise Exception

    def ask_questions_by_function(self):
        if self.function.lower() == 'cut':
            self.ask_how_many_people()
            self.ask_how_many_pizza()
        else:
            self.ask_how_many_people()
            self.ask_pieces_desired_for_each()

    def ask_how_many_people(self):
        self.people = input("How many people? ")
        if not self.people.isdigit():
            raise Exception()
        if self.function == 'cut' and self.people == '0':
            raise Exception()

    def work(self):
        if self.function.lower() == 'cut':
            print(
                f"{self.people} people with {self.pizza} pizza{self.is_plural(int(self.pizza))}\nEach person gets {self.cut_pieces()} piece{self.is_plural(self.cut_pieces())} of pizza.\nThere are {self.leftover_pieces()} leftover pieces.")
        else:
            print(
                f"{self.people} people with {self.pieces} piece{self.is_plural(int(self.pieces))} of pizza desired for each.\nThere should be {self.total_pizza()} pizza{self.is_plural(self.total_pizza())}.")

    def ask_how_many_pizza(self):
        self.pizza = input("How many pizzas do you have? ")
        if not self.pizza.isdigit():
            raise Exception()

    def is_plural(self, number):
        return 's' if number > 1 else ''

    def cut_pieces(self):
        return int(int(self.pizza) * PIECES_PER_PIZZA / int(self.people))

    def leftover_pieces(self):
        return int(int(self.pizza) * PIECES_PER_PIZZA % int(self.people))

    def ask_pieces_desired_for_each(self):
        self.pieces = input("How many pieces of each people? ")
        if not self.pieces.isdigit():
            raise Exception()

    def total_pizza(self):
        total_pieces = int(self.pieces) * int(self.people)
        return int(total_pieces / PIECES_PER_PIZZA) + (1 if total_pieces % PIECES_PER_PIZZA > 0 else 0)


PIECES_PER_PIZZA = 8
