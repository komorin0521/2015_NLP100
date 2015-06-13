inputfilepath=../data/hightemp.txt
if [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi

diffcol1shellfilepath=../result/2_17_diffcol1shell.txt
sort -k1 ../data/hightemp.txt | uniq --check-chars=3 | cut -f1 > $diffcol1shellfilepath

python 2_17_search_different_col1.py \
--inputfilepath=$inputfilepath \
--diffcol1shellfilepath=$diffcol1shellfilepath \
--outputfilepath=../result/2_17_diffcol1.txt
