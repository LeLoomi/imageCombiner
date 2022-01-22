import os
from numpy.random import randint
from PIL import Image


#gen parameters
variations = 6          #+1 to the actual files you have whyever idk dont want to look at it
images_count = -1     #final count, set to -1 to generate all
layers = 4              #before changing adapt coms+layers below


#internal couters
skipped = 0
generated = 0

if images_count == -1:
    images_count = pow(variations - 1, layers)

#create the filename by rolling a random number etc
def generate_filename():
    name = ""
    for int in range(layers):
        name = name + str(randint(1, variations))
    return name

#list that contains all the names
files = []
existing = os.listdir("./output/")


for i in range(images_count):
    name = generate_filename()

    if name not in files and (name + ".png") not in existing:
        files.append(name)

        for item in files:
            layer1 = Image.open(f'./layer1/{item[0]}.png').convert('RGBA')
            layer2 = Image.open(f'./layer2/{item[1]}.png').convert('RGBA')
            layer3 = Image.open(f'./layer3/{item[2]}.png').convert('RGBA')
            layer4 = Image.open(f'./layer4/{item[3]}.png').convert('RGBA')

            com1 = Image.alpha_composite(layer1, layer2)
            com2 = Image.alpha_composite(com1, layer3)
            com3 = Image.alpha_composite(com2, layer4)

            rgb_im = com3.convert('RGB')
            rgb_im.save("./output/" + item + ".png")

        generated = generated + 1
        print("[" + name + "] -> generated")
    else:
        skipped = skipped + 1
        print("[" + name + "] -> skipped")
        continue

print("---------------------------"
      "\nFinal stats:"
      "\nOrdered:   ",images_count,
      "\nGenerated: ",generated,
      "\nSkipped:   ",skipped)