for f in *.zip; do 
    mv -- "$f" "${f%.zip}.cbr"
done
