
from db import BlueStuff
from random import randrange

all_blue_stuff = [
    {
        'name':'Amongus',
        'sprite':'../static/img/amongus_guy.png',
        'attack_name':'stab',
        'damage':20
    },
    {
        'name':'Blastoise',
        'sprite':'../static/img/blastoise.png',
        'attack_name':'water gun',
        'damage':30
    },
    {
        'name':'Blob',
        'sprite':'../static/img/blob.png',
        'attack_name':'wave',
        'damage':15
    },
    {
        'name':'Blue Chungus',
        'sprite':'../static/img/blue_chungus.png',
        'attack_name':'sex',
        'damage':65
    },
    {
        'name':'Stuff',
        'sprite':'../static/img/blue_stuff.jpg',
        'attack_name':"I'm stuff!",
        'damage':20
    },
    {
        'name':'Car',
        'sprite':'../static/img/cachow.jpg',
        'attack_name':'kachow',
        'damage':35
    },
    {
        'name':'Soraka',
        'sprite':'../static/img/Dawnbringer_Soraka.jpg',
        'attack_name':'starcall',
        'damage':100
    },
    {
        'name':'Dva',
        'sprite':'../static/img/dva-overwatch.jpg',
        'attack_name':'pew pew pew',
        'damage':30
    },
    {
        'name':'Eric Cartman',
        'sprite':'../static/img/eric_cartman.jpg',
        'attack_name':'coon attack',
        'damage':55
    },
    {
        'name':'Fantomas',
        'sprite':'../static/img/fantomas.jpg',
        'attack_name':'stab',
        'damage':20
    },
    {
        'name':'Fizz',
        'sprite':'../static/img/Fizz.jpg',
        'attack_name':'SHAAAARK!!!',
        'damage':40
    },
    {
        'name':'genie',
        'sprite':'../static/img/genie.jpg',
        'attack_name':'wish',
        'damage':15
    },
    {
        'name':'Hydreigon',
        'sprite':'../static/img/hydreigon.png',
        'attack_name':'Draco Meteor',
        'damage':100
    },
    {
        'name':'Megamind Guy',
        'sprite':'../static/img/mega_mind.jpg',
        'attack_name':'brain',
        'damage':40
    },
    {
        'name':'M&M',
        'sprite':'../static/img/mnm.png',
        'attack_name':'get eaten',
        'damage':70
    },
    {
        'name':'Mr.Meeseeks',
        'sprite':'../static/img/Mr._Meeseeks.png',
        'attack_name':"I'm Mr.Meeseeks",
        'damage':20
    },
    {
        'name':'Smurf',
        'sprite':'../static/img/smurf.png',
        'attack_name':'smurf',
        'damage':20
    },
    {
        'name':'Star Platinum',
        'sprite':'../static/img/star_platinum.jpg',
        'attack_name':'ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA',
        'damage':90
    },
    {
        'name':'Trundle',
        'sprite':'../static/img/Trundle.jpg',
        'attack_name':'time to troll',
        'damage':85
    },
    {
        'name':'Zorotl',
        'sprite':'../static/img/zorotl.jpeg',
        'attack_name':"I'm blue",
        'damage':60
    },
]

def summon_blue_stuff(id):
    new = randrange(len(all_blue_stuff))
    return BlueStuff(
        name = all_blue_stuff[new]['name'],
        sprite = all_blue_stuff[new]['sprite'],
        attack_name = all_blue_stuff[new]['attack_name'],
        damage = all_blue_stuff[new]['damage'],
        userid = id
    )
