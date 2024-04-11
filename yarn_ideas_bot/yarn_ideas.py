import random

import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.all()
intents.members = True  
intents.messages = True 
# You may need this if your bot needs to access member information

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to generate a random idea based on the specified type
def generate_idea(type):
    if type.lower() == 'crochet':
        ideas = [
          "crochet a scarf that looks like a long piece of bacon",
          "create a crochet pizza with removable toppings",
          "create a fruit hammock",
          "this silly guy -> https://shorturl.at/EFNT3",
          "VOODOO DOLL PINCUSHION -> https://www.supergurumi.com/voodoo-doll-pincushion-crochet-pattern",
          "create a set of crocheted fried egg coasters -> https://www.ravelry.com/patterns/library/fried-egg-coaster",
          "another scarf... yes, seriously, another one.",
          "crochet a set of sushi roll cat toys -> https://amiamour.com/sushi-crochet-pattern-amigurumi-food/",
          "crochet a baby blanket",
          "placemats -> https://www.ravelry.com/patterns/library/mandala-placemats-2",
          "mittens!!!",
          "chicken hat headpiece -> https://www.ravelry.com/patterns/library/chicken-hat-headpiece",
          "crochet hook holder -> https://www.ravelry.com/patterns/library/crochet-hook-holder-4",
          "cactus pincushion -> https://www.ravelry.com/patterns/library/cactus-pincushion-5",
          "nifty needle case! -> https://www.ravelry.com/patterns/library/nifty-needle-case",
          "crochet crown -> https://www.ravelry.com/patterns/library/crown-6",
          "pirate eye patch -> https://www.ravelry.com/patterns/library/pirate-patch",
          "beard -> https://www.ravelry.com/patterns/library/beard-attachment",
          "have you considered a decorative wall hanging",
          "a dog sweater",
          "pot holders! always useful, can't go wrong.",
          "amigurumi... hundreds and hundreds of amigurumi.",
          "gloves but fingerless this time.",
          "cozy slippers for your grandma. or better yet, matching cozy slippers for you and grandma!",
          "heating pad cover?",
          "double thick potholder.",
          "you know, why not another market/tote bag.",
          "hat.",
          "an even bigger blanket than last time.",
          "mini turtle -> https://www.lovecrafts.com/en-us/p/free-mini-turtle-crochet-pattern-by-onefunnymoose",
          "a simple cowl",
          "a light and easy pullover.",
          "the infamous 6 day star blanket",
          "a blanket crocheted with the linen stitch.",
          "a shawl.",
          "crochet a scarf using the v stitch.",
          "granny square pillow.",
          "really lonnnnnnggggg cardigan.",
          "fully matching hat, scarf, cardigan, pantaloon, & socks set",
          "daisy square headband.",
          "a patchwork vest.",
          "a cowboy hat for your cat -> https://www.ravelry.com/patterns/library/cowboy-hat-for-cat",
          "crochet a scrap yarn basket, we both know you need it. https://www.ravelry.com/patterns/library/scrap-yarn-basket",
          "a duck for good luck -> https://www.ravelry.com/patterns/library/good-luck-duck",
          "be mysterious. crochet a ruana.",
          "bucket bag.",
          "a water bottle cozy.",
          "crochet a patchwork lapghan.",
          "a heart wreath -> https://www.lionbrand.com/products/heart-wreath-crochet",
          "an envelope bag! chic!",
          "crochet a beanie using the side saddle stitch.",
          "crochet a scarf with the block stitch.", 
          "crochet a scarf with a tilted square stitch.",
          "crochet a primrose stitch dishcloth",
          "a soap cozy with the iris stitch",
          "a tank top.",
          "swimsuit cover up.",
          "perfect sphere -> https://www.ravelry.com/patterns/library/ideal-sphere",
          "a bucket hat",
          "crochet a steering wheel cover.",
          "yip yips -> https://www.ravelry.com/patterns/library/yip-yips-crochet",
          "crochet a festive table runner.",
          "crochet a throw blanket with jumbo weight yarn",
          "baby booties, awww!",
          "a cardigan.",
          "snood -> https://www.ravelry.com/patterns/library/friend-of-the-forest-hood",
          "tissue box cover. sure, why not.",
          "create some simple & adorable daisy flower coasters.",
          "crochet a case for your ipad or laptop.",
          "a sweater.",
          "crochet a keychain wristlet. -> https://www.youshouldcraft.com/crochet-keychain-wristlet-pattern-free/",
          "coin purse.", 
          "tiny chicken keychain -> https://www.ravelry.com/patterns/library/chicken-amigurumi-keychain",
          "a blanket shrug to keep you warm.",
          "a mug cozy",
          "travel tic tac toe game -> https://www.ravelry.com/patterns/library/tic-tac-toe-travel-game",
          "peas in a pod!!! -> https://www.ravelry.com/patterns/library/peas-in-a-pod-food-friends",
          "crochet a chamomile flower car hanging ornament -> https://www.ravelry.com/patterns/library/chamomile-flower-car-hanging-crochet",
          "balloon animal -> https://www.ravelry.com/patterns/library/dog-balloon-animal",
          "vest with matching hat.",
          "hat with bunny ears for a small child",
          "an adorable bunny -> https://www.ravelry.com/patterns/library/emma-the-bunny",
          "a pointed bonnet",
          "finger puppets! people + pets -> https://www.ravelry.com/patterns/library/finger-puppets-and-pets", 
          "a buckhead waffle throw blanket.",
          "moss stitch socks",
          "silly hand puppets - https://www.ravelry.com/patterns/library/little-cs-silly-hand-puppets",
          "crocodile hand puppet -> https://www.ravelry.com/patterns/library/crocodile-hand-puppet-3",
          "adorable flower cushions -> https://kitzknitz.com/the-retro-throw-pillow-a-free-crochet-pattern/",
          "a hype of geckos ('hype' is the collective noun for a group of geckos)-> https://www.ravelry.com/patterns/library/gecko-3",
          "a granny square afghan",
          "double layer braided cowl.",
          "the early 2000s are back baby, crochet a poncho."
            
        ]
    elif type.lower() == 'knit':
        ideas = [
            "the world's simplest mittens -> https://www.ravelry.com/patterns/library/the-worlds-simplest-mittens",
            "knit a glowing lantern pattern -> https://www.ravelry.com/patterns/library/glowing-compass-lanterns", 
            "a slouchy hat.",
            "knit a scrappy gnome hat.",
            "emotional support chicken ->https://www.ravelry.com/patterns/library/emotional-support-chickentm",
            "frog -> https://www.ravelry.com/patterns/library/frog-48",
          "a cozy pullover -> https://www.lionbrand.com/products/knitting-pattern-adult-raglan-sleeve-pullover-3",
          "a twisty headband -> https://sheepandstitch.com/pattern/how-to-knit-a-twisted-headband-step-by-step-pattern/",
          "holiday sweater!",
          "a classic knit jacket -> https://www.ravelry.com/patterns/library/classic-knit-jacket",
          "knit a book cover.",
          "gloves.",
          "you really can't go wrong with a cardigan.",
          "optical illusion blanket -> https://intheloopknitting.com/trompe-loeil-knitting-patterns.php",
          "hanging plant holder",
          "a colorful vest.",
          "a drawstring camisole -> https://www.ravelry.com/patterns/library/drawstring-camisole",
          "troll slippers -> https://www.ravelry.com/patterns/library/troldetfler---troll-slippers",
          "scrunchie -> https://www.woolandthegang.com/en/products/feeling-good-scrunchie-free-pattern?taxon_id=1524",
          "balletcore is trending, make some leg warmers > www.woolandthegang.com/en/products/wilkinson-leg-warmers-free-pattern",
          "beginner friendly blanket -> https://www.woolandthegang.com/en/products/come-together-blanket-pattern?taxon_id=1524",
          "twinkletoe slippers -> https://www.ravelry.com/patterns/library/twinkletoes",
          "moire for a soiree! https://www.ravelry.com/patterns/library/moire-for-a-",
          "backpack, backpack!",
          "a lil clutch -> https://www.ravelry.com/patterns/library/twilight-clutch",
          "ribbed socks.",
          "tiny little itty bitty newborn baby infant socks.",
          "knit a mermaid tail blanket.",
          "a hot water bottle cover.",
          "knitted dice.",
          "tie behind bag -> https://www.woolandthegang.com/en/products/tie-after-tie-bag-pattern?taxon_id=1524",
          "bonnet?",
          "balaclava?",
          "knit an adorable heart bunting -> https://www.ravelry.com/patterns/library/heart-bunting", 
          "knit a glasses case.",
          "doilies, betch.",
          "catnip mice -> https://www.woolandthegang.com/en/products/mr-jingles-knitting-pattern?taxon_id=1524",
          "potatoes. -> https://www.ravelry.com/patterns/library/potatoes-2",
          "cozy winter cap -> https://www.ravelry.com/patterns/library/cozy-winter-cap-2",
          "a summer heat friendly tanktop -> https://www.ravelry.com/patterns/library/claudia-top-3",
          "a beanie for your friend",
          "cat cocoon -> https://www.ravelry.com/patterns/library/cat-cocoon", 
          "long term project - a temperature blanket (or scarf) -> https://www.ravelry.com/patterns/library/temperature-blanket-2018",
          "a witch hat -> https://www.ravelry.com/patterns/library/witch-hat-22",
          "teddy bear dolls -> https://www.ravelry.com/patterns/library/izzy-teddy-bear-dolls"
        ]
    else:
        return "Invalid type. Please specify 'crochet' or 'knit'."

    return random.choice(ideas)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command to generate an idea
@bot.command()
async def idea(ctx, type: str):
    idea = generate_idea(type)
    await ctx.send(f"{ctx.author.mention} here's an idea for your next {type.lower()} project: {idea}")

# Run the bot with the Discord token
bot.run('{TOKENHERE}')
