tailnum=$1
inputfilepath=../data/hightemp.txt
if [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi
resultshellpath=../result/2_15_tail_shell.txt
tail -$tailnum $inputfilepath > $resultshellpath
python 2_15_tail.py \
--inputfilepath=$inputfilepath \
--resultshellpath=$resultshellpath \
--outputfilepath=../result/2_15_tail_python.txt \
--tailnum=$tailnum
