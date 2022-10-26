def function1 (*args):
    napis = ""
    for arg in args:
        napis +=  f"{arg}-"
    return napis[:-1]


def run_homework():

    napis = function1(1,2,3,4,5)
    print(napis)


if __name__ == '__main__':
    run_homework()