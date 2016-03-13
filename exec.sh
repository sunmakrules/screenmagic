lc=$(cat example.log | wc -l )
echo $lc
tot=1000000
while (($lc < $tot))
do
    python logit.py
done
