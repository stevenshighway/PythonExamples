# Hello World script

def main():
    name = input("Welcome! Please specify your name.")

    provinces = ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]
    province = input("Please specify your province.")

    if province not in provinces:
        print("Invalid province. Available provinces: ", province)
        return

    index = provinces.index(province) + 1

    identity = input("Please specify your Costa Rican ID number.")

    if not identity.isnumeric() or len(identity) != 9:
        print("Please specify a valid ID.")
        return

    if int(identity[0]) != index:
        print("Your ID doesn't seem to match your province. Please try again.")
        return

    print("Hello " + name + "! " +
          "Your ID (" + identity + ") matches the " + province + " province " +
          "due to it's first number being associated to it (", index, ")." +
          "\n" +
          "You may find more information at https://en.wikipedia.org/wiki/C%C3%A9dula_de_identidad_(Costa_Rica)")


main()
