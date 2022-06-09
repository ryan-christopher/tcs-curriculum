'''
clicker game
make a gold counter
make a button
you earn gold for every click
when you have enough gold you can unlock new nodes to automatically generate gold!
'''



from ursina import *

app = Ursina()
window.color = color._20

gold = 0
counter = Text(text='0', y=.25, z=-1, scale=2, origin=(0,0), background=True)
button = Button(text='+', color=color.azure, scale= .125)

def button_click():
    global gold
    gold += 1
    counter.text = str(gold)

button.on_click = button_click



button_2 = Button(cost=10, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold>Gold Generator\n<default>Earn 1 gold every second.\nCosts {button_2.cost} gold.')

def buy_auto_gold():
    global gold
    if gold >= button_2.cost:
        gold -= button_2.cost
        counter.text = str(gold)
        invoke(auto_generate_gold, 1, 1)

button_2.on_click = buy_auto_gold



def auto_generate_gold(value=1, interval=1):
    global gold
    gold += 1
    counter.text = str(gold)
    button_2.animate_scale(.125 * 1.1, duration=.1)
    button_2.animate_scale(.125, duration=.1, delay=.1)
    invoke(auto_generate_gold, value, delay=interval)


def update():
    global gold
    if gold >= button_2.cost:
        button_2.disabled = False
        button_2.color = color.green
    else:
        button_2.disabled = True
        button_2.color = color.gray



app.run()