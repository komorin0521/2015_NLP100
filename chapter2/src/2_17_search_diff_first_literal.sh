sort -k1 ../data/hightemp.txt | uniq --check-chars=3 | cut -f1
