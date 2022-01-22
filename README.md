# imageCombiner
This scripts lets you prepare transparent layers and assemble them into a specified or maximum of possible combinations.

 - Currently works with *exactly* 4 layers and *exactly* 5 possible images per layer, expanding this is a WIP
 - Currently lets you run 2 modes, one to generate all possible combinations (rn 5^4=625) or a specific amount of new combinations, e.g. 10 new ones

For it to work you currently need the main.py in the same direcory as the following folders:
 - "layer1"  *> lowest layer, e.g. background PNGs go here*
 - "layer2"
- "layer3"
- "layer4"  *> top layer, e.g. a hat or hair would go in here*
- "output" *> the folder the script will output the product PNGs into*

*Depending on your enviornment the names yould be case sensitive. The script uses numpy and Pillow.*
