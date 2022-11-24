###########################################
import math
import random
from itertools import product
#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

class Patient:

    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

class Patient:

    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms


    def add_test(self, name: str, results: bool):
        self.test_name = name
        self.test_results = results

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:

    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms


    def add_test(self, name: str, results: bool):
        self.test_name = name
        self.test_results = results

    def has_covid(self):
        if hasattr(self, 'test_name'):
            if self.test_name == 'covid':
                if self.test_results == True:
                    return 0.99
                else:
                    return 0.01

        else:
            prob = 0.05
            # only unique value in case symptoms contain duplicates
            for s in list(set(self.symptoms)):
                if s in ['fever', 'cough', 'anosmia']:
                    prob += 0.1
            return round(prob, 2)

# p1 = Patient('Ken', ['fever', 'anosmia', 'headache', 'fever'])
# p2 = Patient('Lisa', ['sore throat', 'insomnia'])
# p1.add_test('covid', True)
# # p1.add_test('covid', False)
# print(p1.has_covid())
# print(p2.has_covid())
######################

# 2. In this exercise you will make an English Deck class made of Card classes
#
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly.
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

class Deck(Card):
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suit_value_pair = list(product(suits, values))
        self.english = [Card(s_v[0], s_v[1]) for s_v in suit_value_pair]

    def shuffle(self):
        shuffled_deck = random.shuffle(self.english)
        return shuffled_deck

    def draw(self):
        r_i = random.randint(0, len(self.english))
        drawn_card = self.english.pop(r_i)
        return f'Card suit: {drawn_card.suit} value: {drawn_card.value}'
###################

# english_deck = Deck()
# print(english_deck.english)
# print(len(english_deck.english))
# english_deck.shuffle()
# print(english_deck.english)
# print(english_deck.draw())
# print(len(english_deck.english))


# 3. In this exercise you will create an interface that will serve as template
# for different figures to compute their perimeter and surface.

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.
from abc import ABCMeta, abstractmethod

class PlaneFigure(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def compute_perimeter(self):
        return NotImplementedError

    @abstractmethod
    def compute_surface(self):
        return NotImplementedError

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):

    def __init__(self, base: float, c1: float, c2:float, h:float):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        try:
            perimeter = self.c1 + self.c2 + self.base
            return perimeter
        except TypeError:
            raise Exception('Please make sure Trinagle object parameters are float objects!!')

    def compute_surface(self):
        try:
            surface = (self.h * self.base) / 2
            return surface
        except TypeError:
            raise Exception('Please make sure Trinagle object parameters are float objects!!')

# triangle = Triangle(10, 4, 4, 6)
# print('Perimeter:', triangle.compute_perimeter())
# print('Surface:', triangle.compute_surface())

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        try:
            perimeter = 2 * (self.a + self.b)
            return perimeter
        except TypeError:
            raise Exception('Please make sure Rectangle object parameters are float objects!!')

    def compute_surface(self):
        try:
            surface = self.a * self.b
            return surface
        except TypeError:
            raise Exception('Please make sure Rectangle object parameters are float objects!!')

# rectangle = Rectangle(10, 5)
# print('Perimeter:', rectangle.compute_perimeter())
# print('Surface:', rectangle.compute_surface())

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

class Circle(PlaneFigure):

    def __init__(self, radius: float):
        self.radius = radius

    def compute_perimeter(self):
        try:
            perimeter = 2 * math.pi * self.radius
            return perimeter
        except TypeError:
            raise Exception('Please make sure Circle object parameters are float objects!!')

    def compute_surface(self):
        try:
            surface = math.pi * (self.radius ** 2)
            return surface
        except TypeError:
            raise Exception('Please make sure Circle object parameters are float objects!!')

# circle = Circle(10)
# print('Perimeter:', circle.compute_perimeter())
# print('Surface:', circle.compute_surface())
