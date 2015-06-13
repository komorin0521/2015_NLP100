inputfilepath=../data/hightemp.txt
lines=$(wc -l $inputfilepath | cut -d " " -f1)
python 2_10_count_lines.py \
--inputfilepath=$inputfilepath \
--linesnum=$lines
