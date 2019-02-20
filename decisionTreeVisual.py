

# This scripts works fine to save image of a decision tree
# It requries binary target and some table with predictors stored on AB DWH
# It can somehow handle categorical variables - effectively create dummies
# Each dummy then enters as a separate variable into the tree

# Author Martin Macíček


__version__ = 1.0


wget.download

###################################################################################################################
# Import packages


import pandas as pd
import cx_Oracle as cxO
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydotplus

# set path to graphviz environment
# Maybe this will work on your PC - if not set the path manually
import os
os.environ['PATH'].split(os.pathsep)
os.environ['PATH'] += os.pathsep + 'C:\\ProgramData\\Anaconda3\\Library\\bin\\graphviz'
###################################################################################################################

###################################################################################################################
# Load data

# Sample select
sql = """
    SELECT * from ap_risk.mm_python_dec_tree_test_tmp
"""

conn_info = {
            'host': 'DBHDWMN.BANKA.HCI',
            'port': 1521,
            'user': os.getlogin(),
            'psw': input('enter password'),
            'service': 'HDWMN.BANKA.HCI',
        }

conn_str = '{user}/{psw}@{host}:{port}/{service}'.format(**conn_info)

conn = cxO.connect(conn_str, encoding="UTF-8", nencoding="UTF-8")

df = pd.read_sql(sql, con=conn)

conn.close()


# Set what is the name of your target column
target = 'CNT_TARGET_12_60'


###################################################################################################################
# Simple stats

print(df.head(5))

print("Column headings:")
print(df.columns)

print("Average def. rate is {def_rate} with {cnt_defs} defaulters".format(def_rate=df[[target]].mean(), cnt_defs=df[[target]].sum()))
print("Number of rows {nrows} and columns {ncols}".format(nrows=str(df.shape[0]), ncols=str(df.shape[1])))

###################################################################################################################
# Data handling and preparation

# Get column types
column_types = list(zip(df.columns, df.dtypes))
cols_pred_cat = [col_name for col_name, dtype in column_types if dtype.name == 'category' or dtype.name == 'object']
cols_pred_num = [col_name for col_name, dtype in column_types if ('float' in dtype.name) or ('int' in dtype.name)]


df_categorical = df[cols_pred_cat]
df_numerical = df[cols_pred_num]

# Replace nan values
for column in df_numerical:
    print(column)
    df_numerical[column].fillna(-99999, inplace=True)

for column in df_categorical:
    print(column)
    df_categorical[column].fillna('XNA', inplace=True)

# dummies matrix of 0 and 1
one_hot_data = pd.get_dummies(df_categorical, drop_first=True)

# merge them back together
df = df_numerical.join(one_hot_data)
# set target
y = df[target]

# drop target of predictors dataframe
df.drop(target, inplace=True, axis=1)

# get rid of rubbish
del df_categorical, df_numerical, one_hot_data

###################################################################################################################
# Decision Tree settings
criterion = 'gini' # 'gini' or 'entropy'
maxDepth = 4
minSamples = 100
minSamplesLeaf = 50

# inicializuj class
dtree = DecisionTreeClassifier(criterion=criterion, max_depth=maxDepth, min_samples_split=minSamples, min_samples_leaf=minSamplesLeaf)

# pust metodu fit

dtree.fit(df, y)

###################################################################################################################
### Vizualize and Save image


dot_data = StringIO()

export_graphviz(dtree, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,
                feature_names=df.columns[:],
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
