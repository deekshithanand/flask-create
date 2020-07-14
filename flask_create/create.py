# function to create required directories
import os
import shutil


def create():
    temp = os.path.dirname(os.path.realpath(__file__))
    template_dir = os.path.join(temp,'flask_template')
    src_folder = os.path.join(template_dir,'src_dir')

    dest_directory = os.getcwd()

    # dest-src-folder
    dest_src = os.path.join(dest_directory, 'src')

    # copy the files
    shutil.copytree(src_folder, dest_src)

    print("src created")

    # copy other_files
    extras_dir = os.path.join(template_dir,'extras')
    file_list = os.listdir(extras_dir)
    for file_name in file_list:
        full_file_name = os.path.join(extras_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_directory)
    print("Extra files copied.")
    
    #end-message
    print("Setup finished. You can modify the setup freely to your needs!")
    