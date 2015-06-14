inputfilepath=../data/hightemp.txt
if [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi
resultshellpath=../result/2_11_changetabintospace_shell.txt
cat $inputfilepath | sed -e 's/\t/ /g' > $resultshellpath
python 2_11_change_tab_into_space.py \
--inputfilepath=$inputfilepath \
--resultshellpath=$resultshellpath \
--outputfilepath=../result/2_11_changetabintospace_python.txt
