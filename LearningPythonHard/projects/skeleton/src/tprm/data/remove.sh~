PARA_CNT=$#
TRASH_DIR="/home/tuopan/.trash"

for i in $*; do
STAMP=`date +%s`
fileName=`basename $i`
#echo $fileName
mv $i $TRASH_DIR/$fileName.$STAMP
done

