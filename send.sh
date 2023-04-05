shopt -s extglob
sshpass -p "Mark757896" scp -r !(*@(send.sh|clear.sh)) root@159.253.36.173:/var/www/html/lenschess-web-admin-sub


import os
os.system("sshpass -p password scp -o StrictHostKeyChecking=no local_file_path username@hostname:remote_path")