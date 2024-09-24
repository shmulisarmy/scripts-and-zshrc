#!/usr/bin/env bash


# used for quickly making a bash script


touch /Users/Shmuli/scripts/$1
chmod +x /Users/Shmuli/scripts/$1
open -a "visual studio code" /Users/Shmuli/scripts/$1 

echo '#!/usr/bin/env bash' > /Users/Shmuli/scripts/$1
