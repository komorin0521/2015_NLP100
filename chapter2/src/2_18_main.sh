inputfilepath=../data/hightemp.txt

if  [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi

resultshellpath="../result/2_18_reverse_shell.txt"
outputfilepath="../result/2_18_revese_python.txt"

sort -k3 -r $inputfilepath > $resultshellpath

python 2_18_reversesort.py \
--inputfilepath=$inputfilepath \
--resultshellpath=$resultshellpath \
--outputfilepath=$outputfilepath
