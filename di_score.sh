#!/bin/bash
#$0=loop.sh $1=c2smalaga.sumo.cfg $2=malaga-alameda/ $3=tl-logic.add.xml $4=output-tripinfos.xml $5./ $6=200 $7=250
sumo -c $2$1 -a $2$3 
python di_loss.py --trip=$2$4 --netstat=$2$8 > res.txt