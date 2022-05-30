#!/bin/sh

if [ "$(git branch --show-current)" = "main" ]; then
    if [ -z "$(git status --porcelain=v1 2>/dev/null)" ]; then
        echo "SEEK AND DESTROY!!!"
        rm *-sol.ipynb
        rm *\ -\ sol.ipynb
        rm pdfs/*-sol.pdf
        rm pdfs/*\ -\ sol.pdf
        rm -rf *-dev
        rm -rf sol/
        rm docker-compose.yml
        rm Dockerfile
        rm print-pdf.sh
        rm cleanup.sh
    fi
fi


