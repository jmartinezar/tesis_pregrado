#!/bin/bash

lualatex main.tex
biber main
lualatex main.tex
lualatex main.tex