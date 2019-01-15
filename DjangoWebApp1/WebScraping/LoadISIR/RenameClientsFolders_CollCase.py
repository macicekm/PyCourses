
import os
import csv
from tqdm import tqdm # progress bar in console

# all folders in which subfolders need to be modified
folders_dict = {
    # "EprPodaneZaloby": "W:\\Vymahani\\LATE\\EPR\\PODANÉ ŽALOBY", Error .)
    # "EprNachystane": "W:\\Vymahani\\LATE\\EPR\\NACHYSTANÉ", Error .)
    # "EprDebety": "W:\\Vymahani\\LATE\\EPR\\DEBETY", Error .)
    # "ExePodane": "W:\\Vymahani\\LATE\\EXEKUCE\\PODANÉ", Error .)
    # "ExePripravene": "W:\\Vymahani\\LATE\\EXEKUCE\\PŘIPRAVENÉ", Error .)
    # "InsPripravene": "W:\\Vymahani\\LATE\\Insolvence\\PŘIPRAVENÉ", Error .)
    # "InsPrihlasene": "W:\\Vymahani\\LATE\\Insolvence\\PŘIHLÁŠENÉ", Error .)
    # "DED": "W:\\Vymahani\\LATE\\DĚDICKÉ", Error .)
    # "DEDICOVE": "W:\\Vymahani\\LATE\\DĚDICOVÉ", Error .)
    "TEST_EPR": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EPR_PODANE",
    "TEST_EXE": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EXE_PRIPRAVENE"

}


# generate this dictionary from a database in a following way CUID: ID_COLL_CASE
path_to_csv = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\cuidCCTranslator.csv"

with open(path_to_csv) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    clients_dict = {}

    for row in reader:
        clients_dict[row['CUID']] = row['COLL_CASE']


# Deployment code

for folder in folders_dict:
    path_to_folder = folders_dict[folder]
    print(path_to_folder)
    # Get all files in folder
    filenames = os.listdir(path_to_folder)

    for client in tqdm(clients_dict):
        cuid = client
        id_coll_case = clients_dict[client]

        for filename in filenames:  # loop through all files and subfolders in Folder
            if os.path.isdir(
                    os.path.join(os.path.abspath(path_to_folder), filename)):  # check whether the current object is a folder or not

                if filename[filename.rfind(" ")+1:] == str(cuid) and filename.find("CC") == -1:  # check if the CUID in folder name equals client CUID and does not already contain label

                    # DO NOT RUN ON PRODUCTION ONLY YOU REALLY WANT TO RUN IT
                    os.rename(
                        path_to_folder + "\\" + filename,
                        path_to_folder + "\\" + filename + " CC" + str(id_coll_case))
                    print("Found and renamed " + filename + " CC" + str(id_coll_case))


# RollBack code - if anything goes wrong .)

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

                os.rename(
                    path_to_folder + "\\" + filename,
                    path_to_folder + "\\" + filename[:filename.rfind("CC") - 1])

                print("Found and rollbacked " + filename)