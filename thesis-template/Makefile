TARGET = bt_saeki
ABST = resume
TEX = platex
BIB = pbibtex
# BIB = echo
PDF = dvipdfmx

.PHONY: all dvi clean cleanup

all: $(TARGET).pdf $(ABST).pdf

$(ABST).pdf: $(ABST).dvi
	$(PDF) $(ABST)

$(ABST).dvi: $(ABST).aux
	@echo "---------- 2nd level ----------"
	$(TEX) $(ABST).tex
	@echo "---------- 3rd level ----------"
	$(TEX) $(ABST).tex

$(ABST).aux: $(ABST).tex
	@echo "---------- 1st level ----------"
	$(TEX) $(ABST).tex

$(TARGET).pdf: $(TARGET).dvi
	$(PDF) $(TARGET)

dvi: $(TARGET).dvi

$(TARGET).dvi: $(TARGET).bbl
	@echo "---------- 2nd level ----------"
	$(TEX) $(TARGET).tex
	@echo "---------- 3rd level ----------"
	$(TEX) $(TARGET).tex

$(TARGET).bbl: $(TARGET).aux
	@echo "---------- BibTeX ----------"
	-egrep '^[^%]*\\bibliography{.*$$' $(TARGET).tex > /dev/null
	-if [ $$? -eq 0 ]; then \
		$(BIB) $(TARGET); \
	fi

$(TARGET).aux: $(TARGET).tex
	@echo "---------- 1st level ----------"
	$(TEX) $(TARGET).tex

clean:
	rm -f *.aux *.blg *.bbl \
		$(TARGET).lst $(TARGET).log \
		$(TARGET).dvi $(TARGET).out \
		$(ABST).lst $(ABST).log \
		$(ABST).dvi $(ABST).out

cleanup: clean
	rm -f $(TARGET).lof $(TARGET).lot $(TARGET).toc \
		$(TARGET).pdf \
		$(ABST).lof $(ABST).lot $(ABST).toc \
		$(ABST).pdf
