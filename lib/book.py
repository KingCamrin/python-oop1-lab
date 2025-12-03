#!/usr/bin/env python3

class Book:
    '''A Book class'''
    def __init__(self, title, page_count):
        self.title = title
        # Ensure page_count is an integer
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            print("page_count must be an integer")
# Make sure to add a method to turn the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")