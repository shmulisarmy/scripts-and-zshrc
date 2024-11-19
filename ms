

scripts_folder_path="/Users/shmuli/scripts"

fullFileName="$scripts_folder_path/$1"


echo "creating script: " $fullFileName
touch $fullFileName
chmod +x $fullFileName
open -a 'visual studio code' $fullFileName