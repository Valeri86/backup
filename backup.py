import os
import subprocess
from datetime import date

ips = [1,2,3]
SRC_DIR = ""
DST_DIR = ""
USER = "username"
CURRENT_DATE = date.today()
src_directory = " "

src_directory_mapping = {
    1: ['/dir1', '/dir2']
    2: ['/dir1', '/dir2']
    3: ['/dir1', '/dir2']
}

dst_directory_mapping = {
    1: f'/dir3-{CURRENT_DATE}'
    2: f'/dir3-{CURRENT_DATE}'
    3: f'/dir3-{CURRENT_DATE}'
}

for p in ips:
    IP = '1.2.3.' + str(p)

    SRC_DIR = src_directory.join(src_directory_mapping.get(p))
    DST_DIR = dst_directory_mapping.get(p)

    if not os.path.exists(f'{DST_DIR}'):
        os.makedirs(f'{DST_DIR}')

    subprocess.call(['scp', '-r', f'{USER}@{IP}:{SRC_DIR}', DST_DIR])
