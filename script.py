from Colors.ColorsType import *

def main():

    color = Type(255, 255, 255)

    with open("main.color.io", 'w') as f:

        if color.get_r() and color.get_b() and color.get_g()  == 255:
            f.write("White")
        elif color.get_r() and color.get_b() and color.get_g() == 254:
            f.write("Light Grey")

        elif color.get_r() and color.get_g() and color.get_b() == 0:
            f.write("Black")


        f.write(f" R: {color.get_r()}")
        f.write(f" G: {color.get_g()}")
        f.write(f" B: {color.get_b()}")
        f.close()



main()