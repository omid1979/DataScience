#!/bin/bash
while :
do

#mosquitto_pub -t 'sensor/Ammonia2' -u sensor -P sensor -m `shuf -i 22-25 -n1`
#sleep 1

echo	HYDROPSIA0TMP	="617“
echo	HYDROPSIA0PRES="1102“
echo	TETRALINPPSTMP="1183“
echo	TETRALINPPPRES="1097“
echo	PUMPDISCHRGTMP="248“
echo	PUMPDISCHRGPRES="588“
echo	PRESSVALUETMP1="752“
echo	PRESSVALUEPRES1="1082“
echo	PRESSVALUETMP2="592“
echo	PRESSVALUETPRES2="73“
echo	OXYGENPSIATMP="212“
echo	OXYGENPSIAPRES="73“
echo	MIXERTMP1="554“
echo	MIXERPRES1="73“
echo	MIXERTMP2="558“
echo	MIXERPRES2="68“
echo	OXIDATIONRACIN="558“
echo	OXIDATIONRACINPRES="68“
echo	OXIDATIONRACOUT="732“
echo	OXIDATIONRACOUTPRES="63“
echo	DECOMPOSSIONRAC="122“
echo	DECOMPOSSIONRACPRES="58“
echo	ALPIATERELSTRMTMP="337“
echo	ALPIATERELSTRMPRES="53“
echo	ALPIATERELONTMP="450“
echo	ALPIATERELONPRES="45“
echo	SEPARATSTRMTMP="607“
echo	SEPARATSTRMPRES="52“
echo	TETROLONABTMP="604“
echo	TETROLONABPRES="46“
echo	DEHUDROREACTTMP="716“
echo	DEHUDROREACTPRS="40“
echo	NAPHTNVALUETMP="700“
echo	NAPHTNVALUEPRS="35“
echo	PUMPDISCHARG="1“
echo	PRESSURVALUE="1“
echo	OXYGENVALUE="1“
echo	MIXERUPVALUE="0“
echo	MIXERDOWNVALUE="1“
echo	ALPHAMIXER="1“
echo	DEHYDROGENREACTOR="1“


done
