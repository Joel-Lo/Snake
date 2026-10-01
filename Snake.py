import pygame,sys,random, signal, shutil
from pygame.math import Vector2
class Font:
    BOLD = '\033[1m'
    END = '\033[0m'

class Color:
    GREEN = '\033[32m'
    RESET = '\033[0m'

print()

width = shutil.get_terminal_size().columns

print(
    f"{Color.GREEN}{Font.BOLD}"
    + '╔════════════════════════════════════════════════════════════╗'.center(width)
    + '\n'
    + '║                          SNAKE GAME                        ║'.center(width)
    + '\n'
    + '╚════════════════════════════════════════════════════════════╝'.center(width)
    + f"{Font.END}{Color.RESET}"
)

print()

speed = input ("Select game mode: \n1.Normal \n2.Rabbit \n3.Turtle \n4.Cheetah \n5.Pronghorn Antelope \n6.Sloth \n7.Garden Snail \n8. Random \n\nOption ")
print()
choice = input ("Select food: \n1. Apple \n2. Pineapple \n3. Durian \n4. Jackfruit \n5. Watermelon \n6. Mango \n7. Starfruit \n8. Crab \n9. Mouse \n10. Lobster \n11. Random \n\nOption: ")
print()
song = input ("Select music: \n1. Golden (Huntr/x) \n2. Golden (BABYMONSTER) \n3. We Go Up \n4. Wild \n5. Mix \n6. Champion \n7. Random \n\nOption: ")

print()

speedRan = None
choiceRan = None
songRan = None

if speed in ("Random", "8"):
    speedRan = str(random.randint(1, 7))
if choice in ("Random", "11"):
    choiceRan = str(random.randint(1, 10))
if song in ("Random", "7"):
    songRan = str(random.randint(1, 6))

if speed in ("Normal", "1") or speedRan == "1":
    convspeed = "Normal"
elif speed in ("Rabbit", "2") or speedRan == "2":
    convspeed = "Rabbit"
elif speed in ("Turtle", "3") or speedRan == "3":
    convspeed = "Turtle"
elif speed in ("Cheetah", "4") or speedRan == "4":
    convspeed = "Cheetah"
elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
    convspeed = "Pronghorn Antelope"
elif speed in ("Sloth", "6") or speedRan == "6":
    convspeed = "Sloth"
elif speed in ("Garden Snail", "7") or speedRan == "7":
    convspeed = "Garden Snail"
else:
    convspeed = "Normal"

if choice in ("Apple", "1") or choiceRan == "1":
    convchoice = "Apple"
elif choice in ("Pineapple", "2")  or choiceRan == "2":
    convchoice = "Pineapple"
elif choice in ("Durian", "3")  or choiceRan == "3":
    convchoice = "Durian"
elif choice in ("Jackfruit", "4")  or choiceRan == "4":
    convchoice = "Jackfruit"
elif choice in ("Watermelon", "5")  or choiceRan == "5":
    convchoice = "Watermelon"
elif choice in ("Mango", "6")  or choiceRan == "6":
    convchoice = "Mango"
elif choice in ("Starfruit", "7")  or choiceRan == "7":
    convchoice = "Starfruit"
elif choice in ("Crab", "8")  or choiceRan == "8":
    convchoice = "Crab"
elif choice in ("Mouse", "9")  or choiceRan == "9":
    convchoice = "Mouse"
elif choice in ("Lobster", "10")  or choiceRan == "10":
    convchoice = "Lobster"
else:
    convchoice = "Apple"

if song in ("Golden (Huntr/x)", "1")  or songRan == "1":
    convsongname = "Golden"
    convsongaut = "Huntr/x"
elif song in ("Golden (BABYMONSTER)", "2")  or songRan == "2":
    convsongname = "Golden"
    convsongaut = "BABYMONSTER"
elif song in ("We Go Up", "3")  or songRan == "3":
    convsongname = "We Go Up"
    convsongaut = "BABYMONSTER"
elif song in ("Wild", "4")  or songRan == "4":
    convsongname = "Wild"
    convsongaut = "BABYMONSTER"
elif song in ("Mix", "5")  or songRan == "5":
    convsongname = "Music Mix"
    convsongaut = "Huntr/x & BABYMONSTER"
elif song in ("Champion", "6")  or songRan == "6":
    convsongname = "Champion"
    convsongaut = "BLACKPINK"
else:
    convsongname = "Golden"
    convsongaut = "Huntr/x"


title = f"Snake: {convspeed} Edition | {convchoice} Hunt | OST: {convsongname} by {convsongaut}"
pygame.display.set_caption(title)

if song in ("Golden (Huntr/x)", "1") or songRan == "1":
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    pygame.mixer.music.load("Golden - KPop Demon Hunters.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    print ("Activating Golden (Huntr/x)")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
elif song in ("Golden (BABYMONSTER)", "2") or songRan == "2":
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    pygame.mixer.music.load("Golden - BABYMONSTER VER.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    print ("Activating Golden (BABYMONSTER)")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
elif song in ("We Go Up", "3") or songRan == "3":
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    pygame.mixer.music.load("We Go Up.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    print ("Activating We Go Up")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
elif song in ("Wild", "4") or songRan == "4":
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    pygame.mixer.music.load("Wild.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    print ("Activating Wild")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
elif song in ("Mix", "5") or songRan == "5":
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    pygame.mixer.music.load("Mix.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    print ("Activating Mix")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
elif song in ("Champion", "6") or songRan == "6":
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.init()
    pygame.mixer.music.load("Champion.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    print ("Activating Champion")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
else:
    music = "We Go Up.ogg"
    print ("Activating We Go Up")
    print()
    if choice in ("Apple", "1") or choiceRan == "1":
        selection = pygame.image.load('apple.png')
        print ("Activating Apple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Pineapple", "2") or choiceRan == "2":
        selection = selection = pygame.image.load('pineapple.png')
        print ("Activating Pineapple")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Durian", "3") or choiceRan == "3":
        selection = pygame.image.load('durian.png')
        print ("Activating Durian")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Jackfruit", "4") or choiceRan == "4":
        selection = pygame.image.load('jackfruit.png')
        print ("Activating Jackfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Watermelon", "5") or choiceRan == "5":
        selection = pygame.image.load('watermelon.png')
        print ("Activating Watermelon")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mango", "6") or choiceRan == "6":
        selection = pygame.image.load('mango.png')
        print ("Activating Mango")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Starfruit", "7") or choiceRan == "7":
        selection = pygame.image.load('starfruit.png')
        print ("Activating Starfruit")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Crab", "8") or choiceRan == "8":
        selection = pygame.image.load('crab.png')
        print ("Activating Crab")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Mouse", "9") or choiceRan == "10":
        selection = pygame.image.load('mouse.png')
        print ("Activating Mouse")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    elif choice in ("Lobster", "10") or choiceRan == "10":
        selection = pygame.image.load('lobster.png')
        print ("Activating Lobster")
        print()
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")
    else:
        selection = 'apple.png'
        print ("Activating Apple")
        if speed in ("Normal", "1") or speedRan == "1":
            actual_speed = 135
            print("Activating Normal mode")
        elif speed in ("Rabbit", "2") or speedRan == "2":
            actual_speed = 95
            print("Activating Rabbit mode")
        elif speed in ("Turtle", "3") or speedRan == "3":
            actual_speed = 200
            print("Activating Turtle mode")
        elif speed in ("Cheetah", "4") or speedRan == "4":
            actual_speed = 40
            print("Activating Cheetah mode")
        elif speed in ("Pronghorn Antelope", "5") or speedRan == "5":
            actual_speed = 60
            print("Activating Pronghorn Antelope mode")
        elif speed in ("Sloth", "S", "6") or speedRan == "6":
            actual_speed = 250
            print("Activating Sloth mode")
        elif speed in ("Garden Snail", "7") or speedRan == "7":
            actual_speed = 300
            print("Activating Garden Snail mode")
        else:
            actual_speed = 135
            print("Activating Normal mode")

def sigint_handler(sig, frame): 
    if speed in ("Normal", "1") or speedRan == "1": 
        print("\nDeactivating Normal mode")
        print()
        print("Game deactivated") 
        pygame.quit()
        sys.exit() 
    elif speed in ("Rabbit", "2") or speedRan == "2": 
        print("\nDeactivating Rabbit mode")
        print()
        print("Game deactivated") 
        pygame.quit() 
        sys.exit() 
    elif speed in ("Turtle", "3") or speedRan == "3": 
        print("\nDeactivating Turtle mode")
        print()
        print("Game deactivated")  
        pygame.quit() 
        sys.exit() 
    elif speed in ("Cheetah", "4") or speedRan == "4": 
        print("\nDeactivating Cheetah mode")
        print()
        print("Game deactivated")  
        pygame.quit() 
        sys.exit() 
    elif speed in ("Pronghorn Antelope", "5") or speedRan == "5": 
        print("\nDeactivating Pronghorn Antelope mode")
        print()
        print("Game deactivated")  
        pygame.quit() 
        sys.exit() 
    elif speed in ("Sloth", "6") or speedRan == "6": 
        print("\nDeactivating Sloth mode")
        print()
        print("Game deactivated")  
        pygame.quit() 
        sys.exit() 
    elif speed in ("Garden Snail", "7") or speedRan == "7": 
        print("\nDeactivating Garden Snail mode") 
        print()
        print("Game deactivated") 
        pygame.quit() 
        sys.exit() 
    else: 
        print("\nDeactivating Normal mode")
        print()
        print("Game deactivated")  
        pygame.quit() 
        sys.exit() 
        
signal.signal(signal.SIGINT, sigint_handler)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('crunch.ogg')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(fruit,fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0: 
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)            

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        fruit_rect = fruit.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(fruit_rect.left,fruit_rect.top,fruit_rect.width + score_rect.width + 6,fruit_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(fruit,fruit_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()


fruit = selection.convert_alpha()
game_font = pygame.font.Font('PoetsenOne-Regular.ttf', 25)



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, actual_speed)

main_game = MAIN()

swipe_start = None
swipe_threshold = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            swipe_start = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if swipe_start is not None:
                dx = event.pos[0] - swipe_start[0]
                dy = event.pos[1] - swipe_start[1]

                if abs(dx) > abs(dy):
                    if dx > swipe_threshold and main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                    elif dx < -swipe_threshold and main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                else:
                    if dy > swipe_threshold and main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                    elif dy < -swipe_threshold and main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)

                swipe_start = None
        
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)