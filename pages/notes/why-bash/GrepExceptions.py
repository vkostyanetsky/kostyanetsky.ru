import os
import glob

dirname = os.path.dirname(__file__)
dirpath = os.path.abspath(dirname)

log_pathname    = os.path.join(dirpath, '*', '*.log')
log_filenames   = glob.iglob(log_pathname, recursive = True)

output_filename = os.path.join(dirpath, 'result.txt')
output_file     = open(output_filename, 'w', encoding = 'utf-8-sig')

for log_filename in log_filenames:
                                     
    log_file = open(log_filename, 'r', encoding = 'utf-8-sig')
           
    while True:
        
        line = log_file.readline()
    
        if not line:
            break

        if line.find(',EXCP,') != -1:
            output_file.write(line)
    
    log_file.close()

output_file.close()