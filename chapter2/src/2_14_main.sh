headnum=$1
inputfilepath=../data/hightemp.txt
if [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi
resultshellpath=../result/2_14_head_shell.txt
head -$headnum $inputfilepath > $resultshellpath
python 2_14_head.py \
--inputfilepath=$inputfilepath \
--resultshellpath=$resultshellpath \
--outputfilepath=../result/2_14_head_python.txt \
--headnum=$headnum
