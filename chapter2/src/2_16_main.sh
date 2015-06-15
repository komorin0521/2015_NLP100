resultshelldir=../result/2_16_splitfiles/shellresult/
resultpythondir=../result/2_16_splitfiles/pythonresult/
#check the directory of "../result/2_16_splitfiles" exists or not
if [ ! -e ../result/2_16_splitfiles ]; then
    mkdir ../result/2_16_splitfiles
fi

#check the directory $resultshelldir exists in advance
if [ -e $resultshelldir ]; then
    rm -rf $resultshelldir
fi

if [ -e $resultpythondir ]; then
    rm -rf $resultpythondir
fi

#make directory of $resultfshelldir and $resultpythondir
mkdir $resultshelldir
mkdir $resultpythondir

inputfilepath=../data/hightemp.txt

if  [ ! -e $inputfilepath ]; then
    echo $inputfilepath is not found
    exit
fi

splitnum=$1
prefix=$resultshelldir""2_16_split_shell_
split -$splitnum \
--additional-suffix=.txt \
--numeric-suffix \
$inputfilepath \
$prefix

python 2_16_split.py \
--inputfilepath=$inputfilepath \
--resultshelldir=$resultshelldir \
--resultpythondir=$resultpythondir \
--splitnum=$splitnum
