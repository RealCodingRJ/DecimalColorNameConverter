from Colors.ColorsType import *

def main():

    color = Type(0, 0, 0)

    with open("main.color.io", 'w') as f:

        if color.get_r() == 255 and color.get_g() == 235 and color.get_b() == 238:


            f.write(f"Hex: {reddish()}\n")
            f.write("Redish Pink")

        if color.get_r() == 255 and color.get_g() == 0 and color.get_b() == 0:

            f.write(f"Hex: {red()}\n")
            f.write("Red")

        if color.get_r() == 255 and color.get_b() == 255 and color.get_g() == 255:
            f.write(f"Hex: {white()}\n")
            f.write("White")

        if color.get_r() == 254 and color.get_b() == 254 and color.get_g() == 254:
            f.write(f"Hex: {lightgrey()}\n")
            f.write("Light Grey")


        if color.get_r() == 0 and color.get_b() == 0 and color.get_g() == 0:
            f.write(f"Hex: {black()}\n")
            f.write("Black")

        f.write(f" R: {color.get_r()}")
        f.write(f" G: {color.get_g()}")
        f.write(f" B: {color.get_b()}")
        f.close()

main()