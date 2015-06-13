import argparse
import os

def importingargs():
    """
    importing args
    """
    parser = argparse.ArgumentParser(
        description="Split the columns and output the first colum into col1.txt and  the second colum into col2.txt")
    parser.add_argument(
        "--inputfilepath", help="This is the filepath of input file")
    args = parser.parse_args()
    assert args.inputfilepath, "inputfilepath is not found"
    return args.inputfilepath


def splitfilelines(inputfilepath):
    """
    read inputfile and split tab. Then the first colum into colums1 and the second column into colums2
    """

    columns1 = ["%s\n" % line.split("\t")[0]
                for line in open(inputfilepath, "r")]
    columns2 = ["%s\n" % line.split("\t")[1]
                for line in open(inputfilepath, "r")]

    return columns1, columns2


def output(columns1, columns2):
    """
    outputting colums1 into col1.txt and colums2 into col2.txt
    """

    #: cheking the result path "../result"
    resultpath = os.path.join("..", "result")
    if os.path.exists(resultpath) is False:
        os.mkdir(resultpath)

    #: output columns1 into col1.txt
    outputfilepathcolumns1 = os.path.join(resultpath, "col1.txt")
    with open(outputfilepathcolumns1, "w") as f1:
        f1.write("".join(columns1))

    #: output columns\2 into col2.txt
    outputfilepathcolumns2 = os.path.join(resultpath, "col2.txt")
    with open(outputfilepathcolumns2, "w") as f2:
        f2.write("".join(columns2))

    columns1_correctlist = ["高知県\n",
                            "埼玉県\n",
                            "岐阜県\n",
                            "山形県\n",
                            "山梨県\n",
                            "和歌山県\n",
                            "静岡県\n",
                            "山梨県\n",
                            "埼玉県\n",
                            "群馬県\n",
                            "群馬県\n",
                            "愛知県\n",
                            "千葉県\n",
                            "静岡県\n",
                            "愛媛県\n",
                            "山形県\n",
                            "岐阜県\n",
                            "群馬県\n",
                            "千葉県\n",
                            "埼玉県\n",
                            "大阪府\n",
                            "山梨県\n",
                            "山形県\n",
                            "愛知県\n"]

    columns2_correctlist = ["江川崎\n",
                            "熊谷\n",
                            "多治見\n",
                            "山形\n",
                            "甲府\n",
                            "かつらぎ\n",
                            "天竜\n",
                            "勝沼\n",
                            "越谷\n",
                            "館林\n",
                            "上里見\n",
                            "愛西\n",
                            "牛久\n",
                            "佐久間\n",
                            "宇和島\n",
                            "酒田\n",
                            "美濃\n",
                            "前橋\n",
                            "茂原\n",
                            "鳩山\n",
                            "豊中\n",
                            "大月\n",
                            "鶴岡\n",
                            "名古屋\n"]
    #: check the this program is correct or not
    outputcolumns1 = [line for line in open(outputfilepathcolumns1, "r")]
    outputcolumns2 = [line for line in open(outputfilepathcolumns2, "r")]

    assert sorted(outputcolumns1) == sorted(
        columns1_correctlist), "col1.txt is not correct"
    assert sorted(outputcolumns2) == sorted(
        columns2_correctlist), "col2.txt is not correct"


def main():
    print("Start")
    inputfilepath = importingargs()
    columns1, columns2 = splitfilelines(inputfilepath)
    output(columns1, columns2)
    print("Finished")

if __name__ == "__main__":
    main()
