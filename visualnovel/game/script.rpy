define e = Character("Eduardo")
define j = Character("João")

image background = Image("bg.jpg")
image eduardo normal = Image("eduardo normal.png")

label start:

    scene background at center:
        zoom 0.7

    show eduardo normal with moveinleft:
        zoom 0.8
        xalign 0.01
        yalign 1.0

    e "Nothing's perfect, the world's not perfect, but it's there for us, trying the best it can. That's what makes it so damn beautiful."

    j "Once you add a story, pictures, and music, you can release it to the world!"

    return
