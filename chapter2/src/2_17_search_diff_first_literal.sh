sort -k1 ../data/hightemp.txt | uniq --check-chars=3 | cut -f1 > ../result/2_17_result_by_shellscript.txt
