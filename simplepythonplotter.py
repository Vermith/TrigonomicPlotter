import numpy as np
from matplotlib import pyplot as plt

#by Adrian R..

# repeater
choice_quit = input("press q to quit, anything else to continue")
while choice_quit != "q":
    if choice_quit == "q":
        print("Exiting the program...")
    else:
        print("Continuing the program...")

    # creating hub for solvers for each trig ident..
    choice = input("input the shortened versions of the trig identities..")

    # standard trig functions
    # sin
    if choice == "sin":
        # config for the plots
        plt.rcParams["figure.figsize"] = [7.5, 3.50]
        plt.rcParams["figure.autolayout"] = True


        def sintrig(x, co):
            return co * np.sin(x)


        x = np.linspace(-10, 0, 100)

        # data input for plots & showing plot
        plt.plot(x, sintrig(x, int(input('Enter coefficient: '))), color='red')
        plt.show()

    # cos
    elif choice == "cos":
        # config for the plots
        plt.rcParams["figure.figsize"] = [7.5, 3.50]
        plt.rcParams["figure.autolayout"] = True


        def costrig(x, co):
            return co * np.cos(x)


        x = np.linspace(-10, 0, 100)
     # data input for plots & showing plot
        plt.plot(x, costrig(x, int(input('Enter coefficient: '))), color='red')
        plt.show()

    # tan
    elif choice == "tan":
        # config for the plots
        plt.rcParams["figure.figsize"] = [7.5, 3.50]
        plt.rcParams["figure.autolayout"] = True


        def tantrig(x, co):
            return co * np.tan(x)


        x = np.linspace(-10, 0, 100)

        # data input for plots & showing plot
        plt.plot(x, tantrig(x, int(input('Enter coefficient: '))), color='red')
        plt.show()

    # arc versions

    # arcsin
        # config for the plots
        plt.rcParams["figure.figsize"] = [7.5, 3.50]
        plt.rcParams["figure.autolayout"] = True

    elif choice == "arcsin":
        def arcsintrig(x, co):
            return co * np.secsin(x)


        x = np.linspace(-10, 0, 100)

        # data input for plots & showing plot
        plt.plot(x, arcsintrig(x, int(input('Enter coefficient: '))), color='red')
        plt.show()

    # arccos
    elif choice == "arccos":
        # config for the plots
        plt.rcParams["figure.figsize"] = [7.5, 3.50]
        plt.rcParams["figure.autolayout"] = True


        def arccostrig(x, co):
            return co * np.arccos(x)


        x = np.linspace(-10, 0, 100)

        # data input for plots & showing plot
        plt.plot(x, arccostrig(x, int(input('Enter coefficient: '))), color='red')
        plt.show()

    # arctan
    elif choice == "arctan":
        # config for the plots
        plt.rcParams["figure.figsize"] = [7.5, 3.50]
        plt.rcParams["figure.autolayout"] = True


        def arctantrig(x, co):
            return co * np.arctan(x)


        x = np.linspace(-10, 0, 100)

        # data input for plots & showing plot
        plt.plot(x, arctantrig(x, int(input('Enter coefficient: '))), color='red')
        plt.show()

    else:
        print('invaid operations.')
        # Do something based on the user's choice
