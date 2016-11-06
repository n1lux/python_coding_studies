

def kwargs_function(**kwargs):
    """
    kwargs - Keywork args 
    named params
    """
    print(kwargs)
    for k, v in kwargs.items():
        print("{} => {}".format(k, v))


def args_function(*args):
    """
    Sequence  params
    """
    print(args)




kwargs_function(name="nilo", age=33, weigth=94)
args_function("nilo", 32, 94)
