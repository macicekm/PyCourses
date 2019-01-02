

###################################################################################################################
## Import packages

# import libraries

import sklearn.datasets as datasets
import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

import seaborn

# set path to graphviz environment
# Maybe this will work on your PC - if not set the path manually
import os
os.environ['PATH'].split(os.pathsep)

os.environ['PATH'] += os.pathsep + 'C:\\ProgramData\\Anaconda3\\Library\\bin\\graphviz'
###################################################################################################################


###################################################################################################################
# Load data

# Sample select

# SELECT d.cnt_target_12_60
# , to_number(ph.ab_score) AS ab_score, ph.vek
# from owner_dwh.f_loan_at l
# JOIN ap_risk.mm_v_defaults d ON l.skp_loan = d.SKP_LOAN
# JOIN ap_risk.js_base_final js ON l.skp_application = js.skp_application
# JOIN ap_risk.ph_scoring_vector_final ph ON js.skf_approval_process_last = ph.skf
# WHERE d.cnt_target_12_60 >=0
#   AND ROWNUM < 10000
#   ORDER BY dbms_random.value


 # iris=datasets.load_iris()
 # df=pd.DataFrame(iris.data, columns=iris.feature_names)
 # y=iris.target

dfImport = pd.read_excel("TreeSampleData.xlsx", sheet_name="Sheet1")

target = 'TARGET_WITHDRAWN_100'

df = dfImport[[target,'VEK',		'DEPENDENTPERSONNUM',	'CASHLOANSPAYMENTSSUM',	\
               'CREDITLIMITSSUM',	'MLS',	'FLAG_CONFINCOME',	'CREDITAMOUNT',	'AMT_INCOME_MAIN', \
               'SUMUNPAIDPRINCIPAL_FINAL',	'SUMA_SPLATEK_V_BRKI',	'RESIDUALAMOUNT_V_BRKI',	'AB_SCORE',	\
               	'DISPO',	'DTI',	'DSTI',	'BRKI_SCORE',	\
               'AMT_OVERDRAFT_LIMIT',	'DAYS_BETWEEN_ACT_FIRST_UTIL',]]



y = df[target]

###################################################################################################################
# Simple stats

df.head(5)

print("Column headings:")
print(df.columns)

count_row = df.shape[0]  # gives number of row count
count_col = df.shape[1]  # gives number of col count

print(df[['CNT_TARGET_12_60']].mean()) # average default rate
print(df[['CNT_TARGET_12_60']].sum())

print("Number of rows " + str(count_row) + " and columns " + str(count_col))
#print(count_row, count_col)

###################################################################################################################

# Převedení RG na integer

# RGDict = {
#     "A" : 1,
#     "B" : 2,
#     "C" : 3,
#     "D":  4,
#     "E":  5,
#     "F":  6,
#     "G":  7
# }

# Replace nan values
for column in df:
    print(column)
    df[column].fillna(-99999, inplace = True)


# Odstranění některých sloupců

# decision tree zvladne pouze numericke

# For categorical data use this link
# https://stackoverflow.com/questions/38108832/passing-categorical-data-to-sklearn-decision-tree


#del df['SKP_LOAN']
del df[target]


###################################################################################################################
# Decision Tree settings
criterion = 'gini' # 'gini' or 'entropy'
maxDepth = 4
minSamples = 100
minSamplesLeaf = 50

# inicializuj class
dtree= DecisionTreeClassifier(criterion = criterion, max_depth = maxDepth, min_samples_split = minSamples, min_samples_leaf = minSamplesLeaf)

# pust metodu fit

dtree.fit(df, y)

###################################################################################################################
### Vizualize and Save image


dot_data = StringIO()

export_graphviz(dtree, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,
                feature_names= df.columns[:],
                proportion=True
                )


graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

# Create PDF
graph.write_pdf("tree.pdf")

# Create PNG
graph.write_png("tree.png")

# This display works only in Jupyter Notebook
#Image(graph.create_png())
###################################################################################################################
