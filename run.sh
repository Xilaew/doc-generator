#!/bin/bash
./docgen.py
pandoc -s --toc --variable lof --variable lot template_exp.md -o template_exp.tex
pandoc -s --toc template_exp.md -o template_exp.html
pandoc --toc template_exp.md -o template_exp.docx
pandoc template_exp.docx -o template_exp.docx.pdf
xelatex template_exp.tex
evince template_exp.pdf
evince template_exp.docx.pdf