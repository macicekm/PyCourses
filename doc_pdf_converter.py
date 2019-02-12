
# This code will go through all doc like documents in folder and its subdirectories
# converts them to PDF and deletes original versions

# It uses Microsoft word to open a document on background and save it as PDF

# source: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files

import os

from comtypes import client


def doc2pdf(doc):
    """
    convert a doc/docx document to pdf format
    :param doc: path to document
    """
    doc = os.path.abspath(doc) # bugfix - searching files in windows/system32
    name, ext = os.path.splitext(doc)
    try:
        word = client.CreateObject('Word.Application')
        worddoc = word.Documents.Open(doc)
        worddoc.SaveAs(name + '.pdf', FileFormat=17)
    except Exception:
        raise
    finally:
        worddoc.Close()
        word.Quit()



root = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\CHIPO"

for path, subdirs, files in os.walk(root):
    for name in files:
        if name.find(".doc") > 0 and name.find("~$") == -1:

            full_path = os.path.join(path, name)
            print(full_path)
            doc2pdf(full_path)
            os.remove(full_path)


