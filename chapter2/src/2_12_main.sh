resultdir=../result
if [ ! -e $resultdir ]; then
    mkdir ../result
fi
col1shellfilepath=../result/col1_shell.txt
col2shellfilepath=../result/col2_shell.txt
cut -f 1 ../data/hightemp.txt > $col1shellfilepath
cut -f 2 ../data/hightemp.txt > $col2shellfilepath
python 2_12_split_and_output_colums.py \
--inputfilepath=../data/hightemp.txt \
--col1shellfilepath=$col1shellfilepath \
--col2shellfilepath=$col2shellfilepath
