#!/usr/bin/python3
import sys
import os
import io
import re
import random
import string


def generateRandomMarkdownTable(outputStream):
    width = random.randint(2, 5)
    height = random.randint(1, 30)
    outputStream.write('|')
    for x in range(width):
        outputStream.write(
            ''.join([random.choice(string.ascii_letters + string.digits) for n in range(random.randint(2, 5))]))
        outputStream.write('|')
    outputStream.write('\n|')
    for x in range(width):
        outputStream.write('---|')
    for x in range(height):
        outputStream.write('\n|')
        for y in range(width):
            outputStream.write(
                ''.join([random.choice(string.ascii_letters + string.digits + '          ') for n in range(random.randint(2, 20))]))
            outputStream.write('|')


def includeContent(inputURL):
    print(inputURL.group(1))
    with open(inputURL.group(1)) as includeFile:
        return includeFile.read()


def expandMarkdownTemplate(filename, suffix="_exp"):
    with open(filename, "r", encoding="utf-8") as f:
        template = f.read()
    print(template)
    template = re.sub('%%%(.*)%%%', includeContent, template)
    print(template)
    fsep = filename.split(".")
    outFilename = ".".join(fsep[:-1]) + suffix + "." + fsep[-1]
    with open(outFilename, 'w') as outfile:
        outfile.write(template)


for i in range(1, 3):
    print("table" + str(i) + ".md")
    with open("table" + str(i) + ".md", 'w') as out:
        generateRandomMarkdownTable(out)
expandMarkdownTemplate("template.md")
# os.rename("template_exp.md", "Chapters/Chapter2.tex")
