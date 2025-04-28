def greet(name):
    """This function greets the user with the given name.
    Parameters:
    name (str): The name of the user.
    Returns:
    str: A greeting message. """
    return f"Hello, {name}! Welcome."
print(help(greet))

'''
Docstring In Python, a docstring is a string literal that occurs as the first
statement in a module, function, class, or method definition. It is used to
provide documentation about the purpose, usage, and behavior of the module,
function, class, or method. Docstrings are enclosed in triple quotes (either
single or double) and can span multiple lines. They serve as a form of inline
documentation that can be accessed using various tools, such as Python’s
built-in help() function, documentation generators like Sphinx, and integrated
development environments (IDEs) that offer code introspection features.'''