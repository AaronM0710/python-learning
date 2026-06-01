# 'import' loads a module so we can use the functions it provides.
# 'logging' is Python's standard library module for writing log messages.
import logging

# Configure the logging system. This needs to happen once, before any log calls.
#   level=logging.DEBUG — show all messages from DEBUG upward (the lowest level).
#   format=... — controls how each log line looks.
#     %(asctime)s    is the timestamp.
#     %(levelname)s  is the level name like DEBUG, INFO, ERROR.
#     %(message)s    is the actual message you log.
#   The 's' at the end of each placeholder means "format as a string".
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# A debug-level log message marking that the program just started.
# Useful as a breadcrumb so you can see in the output exactly when execution began.
logging.debug('Start of program')


# Define a function that computes the factorial of n (n! = 1 * 2 * 3 * ... * n).
def factorial(n):
    # Log that we just entered factorial(). The %s placeholder gets replaced by the value of n.
    # The '%' operator on a string is the old-style string formatting in Python.
    # 'string with %s' % (value,) substitutes the value into the %s slot.
    logging.debug('Start of factorial(%s)' % (n))

    # Initialize the running total to 1. Multiplying by 1 leaves a number unchanged,
    # so it's the safe starting point for a multiplication accumulator.
    total = 1

    # Loop over the integers in range(n + 1), which is 0, 1, 2, ..., n.
    # NOTE: this is the buggy version from the book. It starts at 0, so total * 0 wipes everything out.
    # The fix shown later in the chapter is: for i in range(1, n + 1):
    for i in range(n + 1):
        # Multiply total by i and store the result back into total.
        # 'total *= i' is shorthand for 'total = total * i'.
        total *= i

        # Log the current iteration's variables so you can watch them change.
        # str(i) converts the integer i to a string so you can concatenate it with the surrounding text.
        logging.debug('i is ' + str(i) + ', total is ' + str(total))

    # Log that we're done with this factorial call, then return the answer.
    logging.debug('End of factorial(%s)' % (n))

    # 'return' sends a value back to whoever called the function.
    return total


# Call factorial(5) and pass the result into print() so it shows up in the output.
# With the bug above, this prints 0 instead of 120.
print(factorial(5))

# Final breadcrumb so you can confirm the program ran all the way to the end.
logging.debug('End of program')
