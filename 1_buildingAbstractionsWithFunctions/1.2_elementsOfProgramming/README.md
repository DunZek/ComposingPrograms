# 1.2 Elements of Programming

- A programming language is more than just
- The language also serves as a framework within which we organize our ideas about computational processes.
- Programs server to communicate those ideas among the members of a programming community.
- Thus, programs must be written for people to read, and only incidentally for machines to execute.
- Every powerful language has three mechanisms for combining simple ideas to form more complex ideas:
    - **primitive expressions and statements**
         - which represent the simplest building blocks that the language provides.
    - **means of combination**
        - by which compound elements are built from simpler ones
    - **means of abstraction**
        -  by which compound elements can be renamed and manipulated as units
- In programming, we deal with two kinds of elements:
    - data - stuff that we want to manipulate
    - functions - describe the rules for manipulating the data
    - (Soon we will discover that they are really not so distinct.)
- Thus, any powerful programming language should be able to describe primitive data and primitive functions,
    - as well as have some methods for combining and abstracting both functions and data.

## 1.2.1 Expressions
- One kind of primitive expression is a number.
- Expressions representing numbers may be combined with mathematical operators to form a compound expression.
- These mathematical expressions use **infix** notation, where the **operator** appears in between the **operands**.

## 1.2.2 Call Expressions
- The most important kind of compound expression is a **call expression**, which applies a function to some arguments
    - The way in which Python expresses function application is the same as in conventional mathematics.
- The **operator** is an expression that precedes parentheses, which enclose a comma-delimited list of **operand** expressions.
- When call expressions are evaluated, we say that the function is **called** with a particular **argument** or sets of arguments, **returning** a value.
- Function notation extends in a straightforward way to **nested** expressions, where the elements are themselves compound expressions.

## 1.2.3 Importing Library Functions
- Python defines a very large number of functions, including the operator functions mentioned in the preceding section, but does not make all of their names available by default. Instead, it organizes the functions and other quantities that it knows about into modules, which together comprise the Python Library.
- The Python 3 Library Docs list the functions defined by each module, such as the math module. However, this documentation is written for developers who know the whole language well.

## 1.2.4 Names and the Environment
- A critical aspect of a programming language is the means it provides for using names to refer to computational objects. If a value has been given a name, we say that the name binds to the value.
- The `=` symbol is called the **assignment** operator in Python (and many other languages).
- Assignment is our simplest means of **abstraction**, for it allows us to use simple names to refer to the results of compound operations.
- The possibility of binding names to values and later retrieving those values by name means that the interpreter must maintain some sort of memory that keeps track of the names, values, and bindings. This memory is called an **environment**.
- In Python, names are often called variable names or **variables** because they can be bound to different values in the course of executing a program.
- When executing an assignment statement, Python evaluates the expression to the right of `=` before changing the binding to the name on the left
- With multiple assignment, all expressions to the right of = are evaluated before any names to the left are bound to those values.
    - As a result of this rule, swapping the values bound to two names can be performed in a single statement.

## 1.2.5 Evaluated Nested Expressions
- To evaluate a call expression, Python will do the following:
    1. Evaluate the operator and operand subexpressions, then
    2. Apply the function that is the value of the operator subexpression to the arguments that are the values of the operand subexpressions.
- The evaluation procedure is **recursive** in nature, that is, it includes, as one of its steps, the need to invoke itself.
- Illustrations that visualize the hierarchical structure of such a process/procedure is called an **expression tree**.
    - The objects at each point in a tree are called nodes; in this case, they are expressions paired with their values.
    - Viewing evaluation in terms of this tree, we can imagine that the values of the operands percolate upward, starting from the terminal nodes and then combining at higher and higher levels.
- We take care of the primitive cases by stipulating that:
    - A numeral evaluates to the number it names,
    - A name evaluates to the value associated with that name in the current environment.
- Environments provide the context in which evaluation takes place, which plays an important role in our understanding of program execution.
- The evaluation procedure does not suffice to evaluate all Python code, only call expressions, numerals, and names.
    - For instance, it does not handle assignment statements.
-  In general, **statements** are not evaluated but executed; they do not produce a value but instead make some change.

## 1.2.6 The Non-Pure Print Function
- Throughout this text, we will distinguish between two types of functions:
    - **Pure functions**. Functions have some input (their arguments) and return some output (the result of applying them).
        - Pure functions have the property that applying them has no effects beyond returning a value.
        - Moreover, a pure function must always return the same value when called twice with the same arguments.
    - **Non-pure functions**. In addition to returning a value, applying a non-pure function can generate side effects, which make some change to the state of the interpreter or computer.
- Chapter 4 will illustrate that pure functions are essential for writing **concurrent** programs, in which multiple call expressions may be evaluated simultaneously.
- Chapter 2 investigates a range of non-pure functions and describes their uses.
