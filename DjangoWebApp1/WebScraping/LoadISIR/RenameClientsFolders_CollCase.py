
import os
import csv
import datetime
from tqdm import tqdm # progress bar in console

dtime_start = datetime.datetime.now()

# all folders in which subfolders need to be modified
folders_dict = {
    "EprPodaneZaloby": "W:\\Vymahani\\LATE\\EPR\\PODANÉ ŽALOBY",
    "EprNachystane": "W:\\Vymahani\\LATE\\EPR\\NACHYSTANÉ",
    "EprDebety": "W:\\Vymahani\\LATE\\EPR\\DEBETY",
    "ExePodane": "W:\\Vymahani\\LATE\\EXEKUCE\\PODANÉ",
    "ExePripravene": "W:\\Vymahani\\LATE\\EXEKUCE\\PŘIPRAVENÉ",
    "InsPripravene": "W:\\Vymahani\\LATE\\Insolvence\\PŘIPRAVENÉ",
    "InsPrihlasene": "W:\\Vymahani\\LATE\\Insolvence\\PŘIHLÁŠENÉ",
    "DED": "W:\\Vymahani\\LATE\\DĚDICKÉ",
    "DEDICOVE": "W:\\Vymahani\\LATE\\DĚDICOVÉ",
    # "TEST_EPR": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EPR_PODANE",
    # "TEST_EXE": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EXE_PRIPRAVENE"
}

# generate this dictionary from a database in a following way CUID: ID_COLL_CASE
# select p.NAME||' '||p.CUID AS FOLDER_NAME, cc.id_coll_case as COLL_CASE
# from coll_case cc
# join person p on cc.id_person = p.id_person

path_to_csv = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\cuidCCTranslator.csv"

with open(path_to_csv) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    clients_dict = {}

    for row in reader:
        clients_dict[row['FOLDER_NAME']] = row['COLL_CASE']


# For log
path_to_log = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\folderRenameLog.csv"
log_file = open(path_to_log, 'w')

log_file.write("DTIME_INSERTED;ACTION;DIRECTORY;FOLDER")  # log header
log_file.write('\n')  # new line



# Deployment code

for folder in folders_dict:
    path_to_folder = folders_dict[folder]
    print(path_to_folder)
    # Get all files in folder
    filenames = os.listdir(path_to_folder)

    for client in tqdm(clients_dict):
        name_cuid = client
        id_coll_case = clients_dict[client]
        filename = path_to_folder + "\\" + name_cuid

        if os.path.exists(filename):

            if filename.find("CC") == -1:  # check if the CUID in folder name equals client CUID and does not already contain label

                # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - BEGIN
                # os.rename(filename, filename + " CC" + str(id_coll_case)) ERRRRRROR
                # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - END

                log_file.write(str(datetime.datetime.now()) + ";Found and renamed;" + folder + ";" + filename + " CC" + str(id_coll_case))
                log_file.write('\n')  # new line

            else:
                log_file.write(str(datetime.datetime.now()) + ";CC already added;" + folder + ";" + filename + " CC" + str(id_coll_case))
                log_file.write('\n')  # new line
        else:
            log_file.write(str(datetime.datetime.now()) + ";Clients folder not found in directory;" + folder + ";" + filename + " CC" + str(id_coll_case))
            log_file.write('\n')  # new line



# RollBack code - if anything goes wrong .)
if False:
    for folder in folders_dict:
        path_to_folder = folders_dict[folder]
        print(path_to_folder)
        # Get all files in folder
        filenames = os.listdir(path_to_folder)

        for filename in tqdm(filenames):  # loop through all the files and folders
            if os.path.isdir(
                    os.path.join(os.path.abspath(path_to_folder),
                                 filename)):  # check whether the current object is a folder or not

                if filename.find("CC") > 0:  # check if there is already a labed

                    # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - BEGIN
                    # os.rename(
                    #     path_to_folder + "\\" + filename,
                    #     path_to_folder + "\\" + filename[:filename.rfind("CC") - 1]) ERRRRRROR
                    # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - END

                    log_file.write(str(datetime.datetime.now()) + ";Found and rollbacked;" + folder + ";" + path_to_folder + "\\" + filename)
                    log_file.write('\n')  # new line


print("Finished, time elapsed = " + str(round((datetime.datetime.now() -dtime_start).total_seconds()/60,2)) + " minutes")