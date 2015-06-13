col1filepath=../result/col1.txt
col2filepath=../result/col2.txt
if ! [ -e $col1filepath ]; then
    echo $col1filepath is not found 
    exit
fi
if ! [ -e $col2filepath ]; then
    echo $col2filepath is not found 
    exit
fi
mergeshellfilepath=../result/2_13_merge_shell.txt
paste $col1filepath $col2filepath > $mergeshellfilepath
python 2_13_merge.py \
--col1filepath=$col1filepath \
--col2filepath=$col2filepath \
--mergeshellfilepath=$mergeshellfilepath \
--outputfilepath=../result/2_13_merge_python.txt

