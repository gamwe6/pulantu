# -*- coding: utf-8 -*-
"""Pulantu

Ubuntu-like release code name, but with plants.

Usage:
        >>> import pulantu
        >>> pulantu.weed()
        'Blushing Boxelder'
"""
import random


PLANTS = {
    'a': ['alder', 'almond', 'ambrosia', 'apple', 'apricot', 'arfaj', 'arrowwood', 'ash', 'azolla',],
    'b': ['bamboo', 'banana', 'baobab', 'bay', 'bean', 'bearberry', 'beech', 'bindweed', 'birch', 'bittercress', 'bittersweet', 'bitterweed', 'blackberry', 'blackhaw', 'blackiehead', 'blueberry', 'box', 'boxelder', 'boxwood', 'brier', 'brittlebush', 'broadleaf', 'buckeye',],
    'c': ['cabbage', 'carrot', 'cherry', 'chestnut', 'chrysanthemum', 'cinnamon', 'clove', 'clover', 'coakum', 'coconut', 'collard', 'columbine', 'colwort', 'coneflower', 'cornel', 'corydalis', 'cress', 'crowfoot', 'cucumber',],
    'd': ['daisy', 'deadnettle', 'dewberry', 'dindle', 'dogwood', 'drumstick', 'durian', 'duscle',],
    'e': ['elderberry', 'eucalyptus', 'eytelia',],
    'f': ['fellenwort', 'felonwood', 'felonwort', 'fennel', 'ferns', 'feverbush', 'feverfew', 'fig', 'flax', 'fluxroot', 'fumewort',],
    'g': ['gallberry', 'garget', 'garlic', 'gilliflower', 'goldenglow', 'gordaldo', 'grapefruit', 'grapevine', 'groundberry', 'gutweed',],
    'h': ['haldi', 'harlequin', 'hellebore', 'hemp', 'hogweed', 'holly', 'houseleek', 'huckleberry',],
    'i': ['inkberry', 'ironwood', 'itchweed', 'ivy',],
    'j': ['jasmine', 'jugflower', 'juneberry', 'juniper',],
    'k': ['keek', 'kinnikinnik', 'kittentai', 'knotweed', 'kousa', 'kudzu', 'kumarahou',],
    'l': ['laceflower', 'lavender', 'leek', 'lemon', 'lettuce', 'lilac',],
    'm': ['maize', 'mango', 'maple', 'mesquite', 'milfoil', 'milkweed', 'moosewood', 'morel', 'mulberry',],
    'n': ['neem', 'nettle', 'nightshade', 'nosebleed',],
    'o': ['olive', 'onion', 'osage', 'osier',],
    'p': ['parsley', 'parsnip', 'pea', 'peach', 'peanut', 'pear', 'pellitory', 'pine', 'pineapple', 'pistachio', 'plantain', 'poisonberry', 'poisonflower', 'poke', 'pokeroot', 'pokeweed', 'polkweed', 'poplar', 'poppy', 'possumhaw', 'potato',],
    'q': ['quercitron',],
    'r': ['ragweed', 'ragwort', 'rantipole', 'rapeseed', 'raspberry', 'redbrush', 'redbud', 'redweed', 'rhubarb', 'ribwort', 'rice', 'roadweed', 'rocket', 'rocketcress', 'rose', 'rosemary', 'rye',],
    's': ['sanguinary', 'saskatoon', 'scoke', 'serviceberry', 'shadblow', 'shadbush', 'silkweed', 'skunkweed', 'snakeberry', 'sneezeweed', 'sneezewort', 'snowdrop', 'sorrel', 'speedwell', 'spoolwood', 'stammerwort', 'stickweed', 'strawberry', 'sugarcane', 'sugarplum', 'sunflower', 'swinies', 'sycamore',],
    't': ['tansy', 'tea', 'thimbleberry', 'thimbleweed', 'thistle', 'thyme', 'tickleweed', 'tomato', 'toothwort', 'trillium', 'tulip', 'tulsi',],
    'u': [],
    'v': ['viburnum', 'violet',],
    'w': ['walnut', 'waybread', 'wheat', 'willow', 'windroot', 'wineberry', 'winterberry', 'wintercress', 'woodbine', 'wormwood',],
    'x': [],
    'y': ['yam', 'yarrow', 'yellowwood',],
    'z': ['zebrawood', 'zedoary',],
}
ADJECTIVES = {
    'a': ['adorable', 'adventurous', 'aggressive', 'agreeable', 'alert', 'alive', 'amused', 'angry', 'annoyed', 'annoying', 'anxious', 'arrogant', 'ashamed', 'attractive', 'average', 'awful',],
    'b': ['bad', 'beautiful', 'better', 'bewildered', 'black', 'bloody', 'blue', 'blushing', 'bored', 'brainy', 'brave', 'breakable', 'bright', 'busy',],
    'c': ['calm', 'careful', 'cautious', 'charming', 'cheerful', 'clean', 'clear', 'clever', 'cloudy', 'clumsy', 'colorful', 'combative', 'comfortable', 'concerned', 'condemned', 'confused', 'cooperative', 'courageous', 'crazy', 'creepy', 'crowded', 'cruel', 'curious', 'cute',],
    'd': ['dangerous', 'dark', 'dead', 'defeated', 'defiant', 'delightful', 'depressed', 'determined', 'different', 'difficult', 'disgusted', 'distinct', 'disturbed', 'dizzy', 'doubtful', 'drab', 'dull',],
    'e': ['eager', 'easy', 'elated', 'elegant', 'embarrassed', 'enchanting', 'encouraging', 'energetic', 'enthusiastic', 'envious', 'evil', 'excited', 'expensive', 'exuberant',],
    'f': ['fair', 'faithful', 'famous', 'fancy', 'fantastic', 'fierce', 'filthy', 'fine', 'foolish', 'fragile', 'frail', 'frantic', 'friendly', 'frightened', 'funny',],
    'g': ['gentle', 'gifted', 'glamorous', 'gleaming', 'glorious', 'good', 'gorgeous', 'graceful', 'grieving', 'grotesque', 'grumpy',],
    'h': ['handsome', 'happy', 'healthy', 'helpful', 'helpless', 'hilarious', 'homeless', 'homely', 'horrible', 'hungry', 'hurt',],
    'i': ['ill', 'important', 'impossible', 'inexpensive', 'innocent', 'inquisitive', 'itchy',],
    'j': ['jealous', 'jittery', 'jolly', 'joyous',],
    'k': ['kind',],
    'l': ['lazy', 'light', 'lively', 'lonely', 'long', 'lovely', 'lucky',],
    'm': ['magnificent', 'misty', 'modern', 'motionless', 'muddy', 'mushy', 'mysterious',],
    'n': ['nasty', 'naughty', 'nervous', 'nice', 'nutty',],
    'o': ['obedient', 'obnoxious', 'odd', 'open', 'outrageous', 'outstanding',],
    'p': ['panicky', 'perfect', 'plain', 'pleasant', 'poised', 'poor', 'powerful', 'precious', 'prickly', 'proud', 'puzzled',],
    'q': ['quaint',],
    'r': ['real', 'relieved', 'repulsive', 'rich',],
    's': ['scary', 'selfish', 'shiny', 'shy', 'silly', 'sleepy', 'smiling', 'smoggy', 'sore', 'sparkling', 'splendid', 'spotless', 'stormy', 'strange', 'stupid', 'successful', 'super',],
    't': ['talented', 'tame', 'tender', 'tense', 'terrible', 'testy', 'thankful', 'thoughtful', 'thoughtless', 'tired', 'tough', 'troubled',],
    'u': ['ugliest', 'ugly', 'uninterested', 'unsightly', 'unusual', 'upset', 'uptight',],
    'v': ['vast', 'victorious', 'vivacious',],
    'w': ['wandering', 'weary', 'wicked', 'wild', 'witty', 'worrisome', 'worried', 'wrong',],
    'x': [],
    'y': [],
    'z': ['zany', 'zealous',],
}
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'z',]

def weed():
    """Return a random release code name"""
    letter = random.choice(LETTERS)
    adjective = random.choice(ADJECTIVES[letter])
    plant = random.choice(PLANTS[letter])
    return '{adjective} {plant}'.format(
        adjective=adjective,
        plant=plant,
    ).title()
