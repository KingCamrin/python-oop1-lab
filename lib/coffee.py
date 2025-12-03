#!/usr/bin/env python3

class Coffee:
    #  define __init__ with size and price parameters
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def __setattr__(self, name, value):
        if name == "size" and value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        super().__setattr__(name, value)

    # define tip method that adds 1 to price and prints a message
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1