inputfilepath=../data/hightemp.txt
if [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi
lines=$(wc -l $inputfilepath | cut -d " " -f1)
python 2_10_count_lines.py \
--inputfilepath=$inputfilepath \
--linesnum=$lines
