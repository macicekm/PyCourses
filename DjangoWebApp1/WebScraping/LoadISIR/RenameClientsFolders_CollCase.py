
import os
import csv
import datetime
from tqdm import tqdm  # progress bar in console

dtime_start = datetime.datetime.now()

# all folders in which subfolders need to be modified

# for testing purposes i moved these folder to my personal testing folder
# use this command in command line xcopy /t /e "C:\Your Folder" "C:\New Folder"
# it does not move files, only folders and subfolders

# xcopy /t /e "W:\Vymahani\LATE\EPR\PODANÉ ŽALOBY" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\EPR_PODANÉ ŽALOBY"
# xcopy /t /e "W:\Vymahani\LATE\EPR\NACHYSTANÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\EPR_NACHYSTANÉ"
# xcopy /t /e "W:\Vymahani\LATE\EPR\DEBETY" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\EPR_DEBETY"
# xcopy /t /e "W:\Vymahani\LATE\EXEKUCE\PODANÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\EXE_PODANÉ"
# xcopy /t /e "W:\Vymahani\LATE\EXEKUCE\PŘIPRAVENÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\EXE_PŘIPRAVENÉ"
# xcopy /t /e "W:\Vymahani\LATE\Insolvence\PŘIPRAVENÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\INS_PŘIPRAVENÉ"
# xcopy /t /e "W:\Vymahani\LATE\Insolvence\PŘIHLÁŠENÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\INS_PŘIHLÁŠENÉ"
# xcopy /t /e "W:\Vymahani\LATE\DĚDICKÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\DĚDICKÉ"
# xcopy /t /e "W:\Vymahani\LATE\DĚDICOVÉ" "D:\Users\mmacicek1695ab\Desktop\Work\Tasks\GITProjects\test\DĚDICOVÉ"


# PROD FOLDERS
# folders_dict = {
#     "EprPodaneZaloby": "W:\\Vymahani\\LATE\\EPR\\PODANÉ ŽALOBY",
#     "EprNachystane": "W:\\Vymahani\\LATE\\EPR\\NACHYSTANÉ",
#     "EprDebety": "W:\\Vymahani\\LATE\\EPR\\DEBETY",
#     "ExePodane": "W:\\Vymahani\\LATE\\EXEKUCE\\PODANÉ",
#     "ExePripravene": "W:\\Vymahani\\LATE\\EXEKUCE\\PŘIPRAVENÉ",
#     "InsPripravene": "W:\\Vymahani\\LATE\\Insolvence\\PŘIPRAVENÉ",
#     "InsPrihlasene": "W:\\Vymahani\\LATE\\Insolvence\\PŘIHLÁŠENÉ",
#     "DED": "W:\\Vymahani\\LATE\\DĚDICKÉ",
#     "DEDICOVE": "W:\\Vymahani\\LATE\\DĚDICOVÉ",
# }

# TEST FOLDERS

folders_dict = {
    "EprPodaneZaloby": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EPR_PODANÉ ŽALOBY",
    "EprNachystane": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EPR_NACHYSTANÉ",
    "EprDebety": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EPR_DEBETY",
    "ExePodane": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EXE_PODANÉ",
    "ExePripravene": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\EXE_PŘIPRAVENÉ",
    "InsPripravene": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\INS_PŘIPRAVENÉ",
    "InsPrihlasene": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\INS_PŘIHLÁŠENÉ",
    "DED": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\DĚDICKÉ",
    "DEDICOVE": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\DĚDICOVÉ",
    # "TEST_EPR": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\TEST_EPR_PODANE",
    # "TEST_EXE": "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\TEST_EXE_PRIPRAVENE"
}

# generate this dictionary from a database in a following way CUID: ID_COLL_CASE
# select p.NAME||' '||p.CUID AS FOLDER_NAME, cc.id_coll_case as COLL_CASE
# from collection_case cc
# join person p on cc.id_person = p.id_person

path_to_csv = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\cuidCCTranslator.csv"

with open(path_to_csv) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    clients_dict = {}

    for row in reader:
        clients_dict[row['FOLDER_NAME']] = row['COLL_CASE']





##############################################################################################################################################################
# Deployment code


print('--X--X--X--X--')
print('Renaming Folders')

# For log
path_to_log = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\folderRenameLog.csv"
log_file = open(path_to_log, 'w')

log_file.write("DTIME_INSERTED;ACTION;DIRECTORY;FOLDER")  # log header
log_file.write('\n')  # new line

for folder in folders_dict:
    path_to_folder = folders_dict[folder]
    print(path_to_folder)

    for client in tqdm(clients_dict):
        name_cuid = client
        id_coll_case = clients_dict[client]
        filename = path_to_folder + "\\" + name_cuid

        if os.path.exists(filename):

            if filename.find("CC") == -1:  # check if the CUID in folder name equals client CUID and does not already contain label

                # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - BEGIN
                os.rename(filename, filename + " CC" + str(id_coll_case))
                # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - END

                log_file.write(str(datetime.datetime.now()) + ";Found and renamed;" + folder + ";" + filename + " CC" + str(id_coll_case))
                log_file.write('\n')  # new line

            else:
                log_file.write(str(datetime.datetime.now()) + ";CC already added;" + folder + ";" + filename + " CC" + str(id_coll_case))
                log_file.write('\n')  # new line
        else:
            try:
                log_file.write(str(datetime.datetime.now()) + ";Clients folder not found in directory;" + folder + ";" + filename + " CC" + str(id_coll_case))
            except:
                log_file.write(str(datetime.datetime.now()) + ";Clients folder not found Exception occurred;" + folder + ";" + " CC" + str(id_coll_case))
            finally:
                log_file.write('\n')  # new line


##############################################################################################################################################################
# Write log of all client folders, that are left and have not been renamed - name does not include CC

print('--X--X--X--X--')
print('Missing CC log')

# For log
path_to_log = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\folderMissedRenameLog.csv"
log_file = open(path_to_log, 'w')

log_file.write("DTIME_INSERTED;ACTION;DIRECTORY;FOLDER")  # log header
log_file.write('\n')  # new line

for folder in folders_dict:
    path_to_folder = folders_dict[folder]
    print(path_to_folder)
    # Get all files in folder
    filenames = os.listdir(path_to_folder)

    for filename in tqdm(filenames):  # loop through all the files and folders
        if os.path.isdir(
                os.path.join(os.path.abspath(path_to_folder),
                             filename)):  # check whether the current object is a folder or not

            if filename.find("CC") == -1:  # check whether label is missing

                try:
                    log_file.write(str(datetime.datetime.now()) + ";CC Label Missing;" + folder + ";" + path_to_folder + "\\" + filename)
                except:
                    log_file.write(str(datetime.datetime.now()) + ";CC Exception occurred;" + folder + ";" + path_to_folder)
                finally:
                    log_file.write('\n')  # new line


##############################################################################################################################################################
# RollBack code - if anything goes wrong .)
if False:

    print('--X--X--X--X--')
    print('Rolling back')

    # For log
    path_to_log = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\folderRollbackLog.csv"
    log_file = open(path_to_log, 'w')

    log_file.write("DTIME_INSERTED;ACTION;DIRECTORY;FOLDER")  # log header
    log_file.write('\n')  # new line

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
                    os.rename(
                        path_to_folder + "\\" + filename,
                        path_to_folder + "\\" + filename[:filename.rfind("CC") - 1])
                    # DO NOT RUN ON PRODUCTION ONLY IF YOU REALLY WANT TO RUN IT - END

                    log_file.write(str(datetime.datetime.now()) + ";Found and rollbacked;" + folder + ";" + path_to_folder + "\\" + filename)
                    log_file.write('\n')  # new line


##############################################################################################################################################################
print("Finished, time elapsed = " + str(round((datetime.datetime.now() -dtime_start).total_seconds()/60, 2)) + " minutes")