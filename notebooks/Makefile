# Find all markdown files recursively
MD_FILES := $(shell find . -type f -name "*.md")
# Convert each .md to .ipynb (same path, different extension)
IPYNB_FILES := $(MD_FILES:.md=.ipynb)
 
# Default target
all: convert
 
# Rule: convert all markdown files
convert: $(IPYNB_FILES)
 
# Explicit rule using a pattern that works with subdirectories
$(IPYNB_FILES): %.ipynb: %.md
	@echo "Converting $< -> $@"
	jupytext "$<" --to notebook -o "$@"
 
# Clean generated notebooks
clean:
	rm -f $(IPYNB_FILES)
 
# Force reconversion
rebuild: clean convert
 
.PHONY: all convert clean rebuild
 
