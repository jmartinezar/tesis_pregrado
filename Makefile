# Variables
MAIN = main
CHAPTERS = chapters/ecuacion_de_Dirac.tex chapters/simetrias_de_gauge.tex chapters/El_mecanismo_de_Higgs.tex
LATEX = lualatex
BIBTOOL = biber
AUX_FILES = $(CHAPTERS:.tex=.aux)
PDF_VIEWER = firefox
figures = figures/pot_1.pdf figures/pot_2.pdf

# Ensure the auxiliary directory exists
.PHONY: all clean distclean view
all: $(MAIN).pdf
	$(PDF_VIEWER) $<

# Build the main document
$(MAIN).pdf: compile.sh main.tex $(AUX_FILES) $(figures)
	./$<

figures/%.pdf: figures/potential_plot.py
	python $<

chapters/%.aux: chapters/%.tex
	lualatex $<

# View the final PDF
view: $(MAIN).pdf
	$(PDF_VIEWER) $(MAIN).pdf &

# Clean auxiliary files
clean:
	rm -rf *.aux *.log *.out \
           *.toc *.bbl *.blg \
           *.run.xml *.bcf *.fls \
           *.fdb_latexmk main.pdf

# Clean everything, including the PDF
distclean: clean
	rm -f $(MAIN).pdf