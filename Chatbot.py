from time import sleep


def indentify_name(text):
    name = str(input(":..."))
    if name == "no quiero decir mi nombre":
        name = str(input("Como quieres que te llame??: "))
    return name


def how_you_feel():
    feel = str(input(":..."))
    return feel


def main():
    text = ("Hola como te llamas")
    print(text)
    name = indentify_name(text)
    if name:
        print("Encantada de conocerte {}".format(name))
        sleep(2)
        print("y pues... dime {} como te sientes hoy?".format(name))
    feel = how_you_feel()
    if feel == "mal" or feel == "me siento un poco mal" or feel == "me siento mal" or feel == "me siento fatal":
        print("Tranquilo todo puede mejorar, solo mantente positivo y todo saldra bien")
    elif feel == "bien" or feel == "me siento realmente bien" or feel == "me siento bien":
        print("INCREIBLEE!! ME ALEGRO MUCHO POR TI!!!")
    elif feel == "no se como me siento realmente" or feel == "no se" or feel == "no lo se":
        print("relajate un poco, quiza estes en un momento de estres o te preocupen \n"
              "algunas cosas pero...eres fuerte y se que podras seguir adenlante")

if __name__ == "__main__":
    main()