""" 1.1 Getting Started
    - All computing begins with:
        1. Representing information
        2. Specifying logic to process it
        3. Desigining abstractions that manage the complexity of that logic
"""
# You must learn how computers interpret programs and carry out the computational process

""" 1.1.1 Programming in Python
    - Python will be used to define computational processes because both man and machine can understand it
    - The language is a large open-source project
        - It was started by Guido van Rossum in the late 80s
    - The Zen of Python guides by the principles of beauty, simplicity, and readability

    - The SICP fashion dictates that Python will be introduced step-by-step with techniques for:
        - Abstraction and
        - A rigorous model of computation
"""

# 1.1.2 Installing Python 3 - Python 3 will be used in this book

""" 1.1.4 First Example """
from urllib.request import urlopen

# Statements & Expressions - that which Python code consists of where programs instruct to either
#   1. Compute some value
#   2. Carry out some action

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
