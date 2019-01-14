
import os
#import csv
from tqdm import tqdm # progress bar in console

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
    "TEST_EPR": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EPR_PODANE",
    "TEST_EXE": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EXE_PRIPRAVENE",
    "csv_with_clients" : "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\clientCodesTranslator.csv"
}

# generate this dictionary from a database in a following way CUID: ID_COLL_CASE
clients_dict = {2: 3,
                5:6,
                8:9,
                11:12,
                14:15
}


path_to_csv = folders_dict["csv_with_clients"]
path_to_folder = folders_dict["TEST_EPR"]



# with open(path_to_csv) as f:
#     reader = csv.reader(f)
#     clients_list = list(reader)

# Get all files in folder
filenames = os.listdir(path_to_folder)

for client in tqdm(clients_dict):
    cuid = client
    id_coll_case = clients_dict[client]

    for filename in filenames:  # loop through all the files and folders
        if os.path.isdir(
                os.path.join(os.path.abspath(path_to_folder), filename)):  # check whether the current object is a folder or not

            if filename.find(str(cuid)) != -1 and filename.find("CC") == -1:  # check if the folder name contains client CUID and does not already contain label
                print("Found and renamed " + filename)
                os.rename(
                    path_to_folder + "\\" + filename,
                    path_to_folder + "\\" + filename + " CC" + str(id_coll_case))
