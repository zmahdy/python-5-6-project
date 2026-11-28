# code ruasabilty , code organization , readability , maintainability , less repeatation  testing
#  def , functions : 2 build in fun : pirnt(), len(), user define :
#  def nameoffunctin():
# body of fun

#  nameing rols of function : snake_case 2name ,add number,


# calling function
# prameter :*arg :  argument positional , keyword , defualt: return print()

number = 30  # global


def view():
    global number  # noqa: PLW0602
    print("global ", number)

    print(number + 1)


view()
print(number)
