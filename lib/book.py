#!/usr/bin/env python3

class Book:
    '''A Book class'''
    def __init__(self, title, page_count):
        # use __setattr__ for validation
        self.title = title
        self.page_count = page_count

    def __setattr__(self, name, value):
        if name == "page_count" and not isinstance(value, int):
            print("page_count must be an integer")
        # always set the value
        super().__setattr__(name, value)

    # Make sure to add a method to turn the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")