""" 1.1 Getting Started
    - Computer science is terribly broad: Distrib-sys, AI, robo, graph, secur, sci-compute, comp-arch
    - Few parts of human life is unaffected: commerce, comm, sci, art, leisure, politics <- computational domains
    - Why is comp-sci powerful? Because of elegant and powerful fundamental ideas:
        1. Representing information
        2. Specifying logic to process it
        3. Designing abstractions that manage the complexity of that logic
    - Such ideas everything computing, computer, and computer science have long been taught using SICP.
    - This book borrows heavily from that textbook.
"""
# You must learn how computers interpret programs and carry out the computational process

""" 1.1.1 Programming in Python
    - Python will be used to define computational processes because both man and machine can understand it
    - Pythonistas -> web-devs, game-devs, scientists, academics, lang-designers, million-person-strong community
    - Dev communities -> solve probs, share projs/exp, dev software/tools
    - The language is a large open-source project. It was started by Guido van Rossum in the late 80s
    - The Zen of Python guides by the principles of beauty, simplicity, and readability
    - Good for learning because of readability and features which enable numerous programming styles
    - The SICP fashion dictates that Python will be introduced step-by-step with techniques for:
        - abstraction
        - rigorous model of computation
"""

# 1.1.2 Installing Python 3 - Python 3 will be used in this book
# 1.1.3 Interactive Sessions - just some REPL-ing

""" 1.1.4 First Example
    - Python will be introduced by building up language knowledge piece-by-piece
    - Python capabilities -> text-manip, displ-graphics, internet comm.
"""
from urllib.request import urlopen  # <- loading internet-comm. functionality by enabling a function that can access content via uniform resource locator

# Statements (actions which are carried out) & Expressions (computations which are evaluated) - that which Python code consists of where programs instruct to either:
#   1. Compute some value
#   2. Carry out some action
shakespeare = urlopen("http://composingprograms.com/shakespeare.txt")  # a statement

# Functions - encapsulators of data-manipulating logic (Featured in chapter 1, this chapter)
words = set(shakespeare.read().decode().split())  # furthermore statements but using more functions
# ^^ read data from URL, decode data into text, split text into words, put words into a set and assign it to "words" variable

# Objects - a complexity-management bundle of data and logic used to manipulate said data (Featured in chapter 2)
print( {w for w in words if len(w) == 6 and w[::-1] in words} )  # an expression - evalutes to the set of all words that are sinultaneously a word spelled in reverse

# Interpreters - a program that interprets human-readable code. It carries out statements and evaluates expressions (Featured in Chapter 3).
# Computer programs do not compare to the unique generality of interpreters. The Python interpreter allows inherently cumbersome code to be expressed in small volumes
# All of the aforementioned concepts are related:
#   functions are objects,
#   objects are functions and
#   interpreters are instances of both
# Strive to develop the fundamental philosophy behind each of these concepts to master the art of programming

""" 1.1.5 Errors
    - Computers are fast as they are rigid.
    - Within Standford's introductory course (CS101):
        - The fundamental equation of computers -> "computer = powerful + stupid".
        - Computers can process tremendous volumes of data and perform billions of operations per second.
        - Computers are also extremely stupid and fragile. All it takes is one unhandled error or uncatched exception to cease operations and crash the computer.

    - Programming is about a person constructing useful things out of the tiny, simple little operations that a computer can do using their personal insights.
"""
# Many unexpected errors are caused by simple spelling and formatting mistakes within the code
# Debugging is the process of interpreting and diagnosing errors. It is mostly guided by the following principles
# 1. Test incrementally - Divide the program into manageable subcompositions which must be debugged ASAP before continuing development
# 2. Isolate errors - Trace errors to the smallest fragment of code located within the particular modular component attributed by the error-output
# 3. Check your assumptions - Unexpected behavior can and will with time, arise from the programmer's false assumption and insight used to write the code and generate the program.
# 4. Consult others - Research. Procure enabling knowledge from external resources and then return to the problem at hand. Ask either man or machine.

# Test incrementally, design out of modularity, use critical assumptions, and teamwork to make the dreamwork
# Let such themes persist in your computer science career.
