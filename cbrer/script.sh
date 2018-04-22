#!/bin/bash
rm -r cbr
mkdir cbr
cp urls.txt cbr/urls.txt
cd cbr/

i=0
for url in `cat urls.txt`
do
  curl -o $i".jpg" -O $url
  ((i++))
done

rm urls.txt
cd ..

zip -r comic.zip cbr
for f in comic.zip; do 
    mv -- "$f" "${f%.zip}.cbr"
done

rm -r cbr/

echo Done
