import os
from numpy.random import randint
from PIL import Image

# gen parameters
variations = 5
layers = 4  # before changing, adapt coms+layers below

# internal counting
order_count = 0
skipped = 0

order_count_stat = 0
iterations_stat = 0
generated_stat = 0
skipped_stat = 0


# create the filename by rolling a random number etc
def generate_filename_random():
    name = ""
    for i in range(layers):
        name = name + str(randint(1, variations + 1))
    return name


# list that contains all the names
files_generated = []
existing_files = os.listdir("./output/")


def generate_complete_collection():
    # to tell user the no. of image in console etc.
    progress = 0
    global generated_stat
    global skipped_stat
    global iterations_stat

    # count the digits for clean progression output
    digits = sum(c.isdigit() for c in str(order_count))

    for l1 in range(variations):
        for l2 in range(variations):
            for l3 in range(variations):
                for l4 in range(variations):
                    progress += 1
                    iterations_stat += 1

                    name = str(l1 + 1) + str(l2 + 1) + str(l3 + 1) + str(l4 + 1)  # assemble filename from the fors
                    if name not in files_generated and (
                            name + ".png") not in existing_files:  # check if file already exists (to skip)
                        files_generated.append(name)

                        for item in files_generated:
                            layer1 = Image.open(f'./layer1/{item[0]}.png').convert('RGBA')
                            layer2 = Image.open(f'./layer2/{item[1]}.png').convert('RGBA')
                            layer3 = Image.open(f'./layer3/{item[2]}.png').convert('RGBA')
                            layer4 = Image.open(f'./layer4/{item[3]}.png').convert('RGBA')

                            com1 = Image.alpha_composite(layer1, layer2)
                            com2 = Image.alpha_composite(com1, layer3)
                            com3 = Image.alpha_composite(com2, layer4)

                            rgb_im = com3.convert('RGB')
                            rgb_im.save("./output/" + item + ".png")

                        generated_stat += 1
                        print("[" + str(name) + " | " + str(progress).zfill(digits) + "/" + str(
                            order_count) + "] -> generated")

                    else:
                        skipped_stat += 1

                        print("[" + str(name) + " | " + str(progress).zfill(digits) + "/" + str(
                            order_count) + "] -> skipped")


def generate_random_collection():
    global skipped
    global skipped_stat
    global order_count
    global generated_stat
    global iterations_stat

    # to tell user the no. of image in console etc.
    progress_stat = 0
    # count the digits for clean progression output
    digits = sum(c.isdigit() for c in str(order_count))

    for i in range(order_count):
        progress_stat += 1
        iterations_stat += 1

        name = generate_filename_random()

        if name not in files_generated and (name + ".png") not in existing_files:
            files_generated.append(name)

            for item in files_generated:
                layer1 = Image.open(f'./layer1/{item[0]}.png').convert('RGBA')
                layer2 = Image.open(f'./layer2/{item[1]}.png').convert('RGBA')
                layer3 = Image.open(f'./layer3/{item[2]}.png').convert('RGBA')
                layer4 = Image.open(f'./layer4/{item[3]}.png').convert('RGBA')

                com1 = Image.alpha_composite(layer1, layer2)
                com2 = Image.alpha_composite(com1, layer3)
                com3 = Image.alpha_composite(com2, layer4)

                rgb_im = com3.convert('RGB')
                rgb_im.save("./output/" + item + ".png")

            print("[" + str(name) + " | " + str(progress_stat).zfill(digits) + "/" + str(order_count) + "] -> generated")
            generated_stat += 1

        else:
            skipped += 1
            skipped_stat += 1
            print("[" + str(name) + " | " + str(progress_stat).zfill(digits) + "/" + str(order_count) + "] -> skipped")

            # to create another one after this run since we'd be 1 down every skip otherwise
            order_count += 1
            continue

    # to create the "missing" ones to actually gen 10 if 10 ordered by user
    if 0 < skipped <= pow(variations, layers):
            order_count = skipped
            skipped = 0

            generate_random_collection()


print("---------------------------"
      "\nSet up for", variations, "variations &", layers, "layers"
      "\n\nSelect to continue:"
      "\n 1: Create all possible combinations"
      "\n 2: Create a random collection"
      "\n 3: Exit program")

while True:
    mode = input("Selection » ")

    if mode == "1":
        order_count = pow(variations, layers)
        generate_complete_collection()
        break
    elif mode == "2":
        order_count = int(input("Count of images to generate: "))
        generate_random_collection()
        break
    elif mode == "3":
        raise SystemExit(0)
    else:
        print("\u26A0 Faulty input")
        continue

print("---------------------------"
      "\nFinal statistics:"
      "\nIterations: ", iterations_stat,
      "\nGenerated:  ", generated_stat,
      "\nSkipped:    ", skipped_stat)
