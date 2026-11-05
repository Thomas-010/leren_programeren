from challenges.solutions import *
from random import randint, shuffle

all_colors = 'rgbypownl'
def random_color_list(colors, length):
    shuffled_colors = list(colors)
    shuffle(shuffled_colors)
    return [shuffled_colors[index] for index in range(length)]

challenges = {
    1 : {
        'name':'grab the color that is different',
        'start' : 'x,x,x,x,x,x,x,x,x,x', 
        'symbols': (lambda colors: 'x-'+(colors[0]*9)+colors[1] )(random_color_list(all_colors, 2))
    },
    2 : {
        'name':'at the left order from most to lowest',
        'start' : ',,,,x,x,x,x,x,x', 
        'symbols': (lambda colors: 'x-'+(colors[0]*3)+(colors[1]*2)+colors[2] )(random_color_list(all_colors, 3))
    },
    3 : {
        'name':'sort the colors on the outside, 2 on each side',
        'start' : ',,,xxxx,xxxx,xxxx,xxxx', 
        'symbols': (lambda colors: 'x-'+(''.join(colors)*4))(random_color_list(all_colors, 4))
    },
    4 : {
        'name':'create two the same stacks',
        'start' : 'xxxx,,,,,,y,y,y,y',
        'symbols': (lambda colors: 'y-'+''.join(colors)+',x-'+''.join(colors) )(random_color_list(all_colors, 4))
    },
    5 : {
        'name':'stack the double color',
        'start' : 'x,x,x,x,x,x,x,x,x,x', 
        'symbols': (lambda colors: 'x-'+colors+colors[randint(0,len(colors)-1)] )(all_colors)
    },
}
