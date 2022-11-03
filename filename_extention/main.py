import os

file_name = "data/sample_dir/test.txt"
file_name_withex = os.path.basename(file_name)
file_name_noex = os.path.splitext(file_name_withex)[0]

print(file_name_withex)
print(file_name_noex)