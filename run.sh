#!/bin/bash
./docgen.py
pandoc -N --pdf-engine=xelatex --toc -o example14.pdf
pandoc template_exp.md -o simple.pdf
#pdflatex simple.tex
evince simple.pdf