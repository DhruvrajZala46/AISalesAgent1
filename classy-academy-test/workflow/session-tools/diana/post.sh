T=/home/user/AISalesAgent1/classy-academy-test/workflow/tools
cd /tmp/claude-0/-home-user-AISalesAgent1/140e17c2-af15-50d0-a685-731162836c6b/scratchpad/cdi
python3 pshots.py > shots.log 2>&1
touch stripped.txt
keys=$(ls raw | grep '\.mp4$' | grep -v tmp | sed 's/\.mp4//' | grep -vxFf stripped.txt | tr '\n' ' ')
if [ -n "$keys" ]; then python3 strips2.py st/$1 $keys > strips_$1.log 2>&1; echo $keys | tr ' ' '\n' >> stripped.txt; fi
echo STRIPSDONE >> strips_$1.log
bash _dur.sh > dur.log 2>&1
python3 $T/dupall.py > dupall.log 2>&1
python3 oldclash.py > oldclash.log 2>&1
python3 $T/aiscan.py > aiscan.log 2>&1
echo POSTDONE $1 >> aiscan.log
