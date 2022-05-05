import shutil
from datetime import datetime

# Get active window path from txt tile
with open('path.txt') as f:
    pathContent = f.read()

# Get current date and time
now = datetime.now()
dt_string = now.strftime("(%H:%M)")
dt_string = dt_string.replace(":", ",")
dt_string = str(dt_string)

# Check to see if other copies exist and assign latest a number
import os.path as pth
filenum = 1
while (pth.exists(pathContent+ "_BACKUP_" + str(filenum) + "_" + dt_string + ".blend")):
    filenum+=1

# Create the backup file
shutil.copy2(pathContent + '.blend', pathContent + "_BACKUP_" + str(filenum) + "_" + dt_string +'.blend')
