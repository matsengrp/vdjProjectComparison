#This file contains the commands to run the biobox encased project Mixcr
python inputDir/MixcrYamlFileGenerator.py
mv biobox.yml ./inputDir 
docker build -t bioboxmixcr ./bioboxmixcr
docker run --volume="$(pwd)/inputDir:/bbx/input:ro" --volume="$(pwd)/outputDir:/bbx/output:rw" bioboxmixcr 
