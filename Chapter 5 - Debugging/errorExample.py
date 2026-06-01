# Define a function called spam. It takes no arguments (empty parentheses).
# The 'def' keyword introduces a function; the body is indented underneath.
def spam():
    # Inside spam(), we call another function called bacon().
    # This creates a chain of calls — spam calls bacon — which is what makes the traceback interesting.
    bacon()


# Define a function called bacon. Also takes no arguments.
def bacon():
    # 'raise' creates and throws an Exception. Because no try/except wraps this call,
    # the exception will propagate up through bacon, then up through spam, then crash the program.
    # When that happens, Python prints a traceback showing the full chain of calls.
    raise Exception('This is the error message.')


# Call spam() to kick off the chain. spam calls bacon, bacon raises, program crashes.
# The traceback will show: error happened on line 5 (the raise), called from line 2 (spam's body),
# called from line 13 (this line right here, where the chain started).
spam()
