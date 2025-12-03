#!/usr/bin/env python3

class Coffee:
#  define __init__ with size and price parameters
    def __init__(self, size, price):
        if size in ["Small", "Medium", "Large"]:
            self.size = size
        else:
            print("size must be Small, Medium, or Large")
        self.price = price
# define tip method that adds 1 to price and prints a message
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1