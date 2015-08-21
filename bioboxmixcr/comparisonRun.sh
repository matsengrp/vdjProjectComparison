#This file contains the commands to run the biobox encased project Mixcr
#python inputDir/MixcrYamlFileGenerator.py
#mv biobox.yml ./inputDir 
docker build -t bioboxmixcr ./bioboxmixcr
docker run --volume="$(pwd)/bioboxmixcr/inputDir:/bbx/input:ro" --volume="$(pwd)/bioboxmixcr/outputDir:/bbx/output:rw" bioboxmixcr 
echo bioboxmixcr: $(pwd)/bioboxmixcr/outputDir/output.txt > dataFile.txt
