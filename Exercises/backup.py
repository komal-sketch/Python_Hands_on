# f = formatted string
import os
import shutil
import datetime

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name,'gztar', source)

source = "source path"
destination = "destination path"

backup_files(source,destination)
