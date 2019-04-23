#!/bin/bash
rm -f template_exp*
./docgen.py

pandoc -s --template pandoc-template.latex metadata.yml template_exp.md -o template_exp.pdf
pandoc -s --template pandoc-template.latex metadata.yml template_exp.md -o template_exp.tex
ln --symbolic template_exp.tex template_exp.xetex.tex
#ln --symbolic template_exp.tex template_exp.pdftex.tex
latexmk -quiet -xelatex template_exp.xetex.tex
#pdflatex template_exp.pdftex.tex
#pdflatex template_exp.pdftex.tex

#pandoc -s --toc template_exp.md -o template_exp.html

pandoc --toc template_exp.md -o template_exp.docx
pandoc template_exp.docx -o template_exp.docx.pdf

evince template_exp.pdf &
evince template_exp.xetex.pdf &
#evince template_exp.pdftex.pdf &
#evince template_exp.docx.pdf &
#firefox template_exp.html &
