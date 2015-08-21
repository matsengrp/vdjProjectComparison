#This file contains the commands to run the biobox encased project Mixcr
#8-20-15
#================
#generate input yaml file and move to input directory
#python inputDir/MixcrYamlFileGenerator.py
#mv biobox.yml ./inputDir
#================
#run docker commands 
docker build -t bioboxmixcr ./bioboxmixcr
docker run --volume="$(pwd)/bioboxmixcr/inputDir:/bbx/input:ro" --volume="$(pwd)/bioboxmixcr/outputDir:/bbx/output:rw" bioboxmixcr 
#================
#run plot performance on this biobox
#python plotPython/mixcrparser.py
plotDir=$(python ./bioboxmixcr/plotPython/mixcrparser.py)
plotDir=$plotDir | rev | cut -d ' ' -f2 | rev
#================
#write name of biobox and corresponding path to output file into file containing address
echo bioboxmixcr:$(pwd)/bioboxmixcr/plotPython/$plotDir > dataFile.txt


