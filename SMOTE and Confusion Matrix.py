import pandas as pd
import numpy  as np
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

#load the data
test_data = pd.read_csv("/Users/mac/My files/jobs/R.com/test_reviews[6].csv")

#missing values
test_data.isnull().sum()

#Remove location-if we include location while segregating training and test
#we have only 3 locations in training but we have 4 locations in test.
test_data=test_data.drop('location_id',1)

#Separating test and training data
test_data_test=test_data[test_data['rating'].isnull()]
print('Shape of test data',test_data_test.shape)

test_data = test_data[np.isfinite(test_data['rating'])]
print('Shape of training data',test_data.shape)



#extract year, month and day separately
test_data['year'] = pd.to_datetime(test_data['date']).dt.year
test_data['month'] = pd.to_datetime(test_data['date']).dt.month
test_data['day'] = pd.to_datetime(test_data['date']).dt.day


#converting source into a factor by using get dummies
temp1=pd.get_dummies(test_data['source'],drop_first=True)
test_data=pd.concat([test_data,temp1],axis=1)
test_data=test_data.drop('source',1)


#remove review id & date once we have extracted the information
test_data=test_data.drop('review_id',1)
test_data=test_data.drop('date',1)


#convert features to category
test_data['FACEBOOK']=test_data['FACEBOOK'].astype('category')
test_data['GOOGLE_PLACES']=test_data['GOOGLE_PLACES'].astype('category')
test_data['year']=test_data['year'].astype('category')
test_data['month']=test_data['month'].astype('category')
test_data['day']=test_data['day'].astype('category')
print("final data type of features",test_data.dtypes)

############################################
# Creating dependent and independent variables
x=test_data[test_data.columns[1:6]]
x.head()
y=pd.DataFrame(test_data[test_data.columns[0]])
y=y['rating'].astype('category')
y.head()





################################
#Machine learning
################################



# Function to calculate accuracy,precisoin,recall and f1 score 
def print_results(headline, true_value, pred):
    print(headline)
    print("accuracy: {}".format(accuracy_score(true_value, pred)))
    print("precision: {}".format(precision_score(true_value, pred,average='weighted')))
    print("recall: {}".format(recall_score(true_value, pred,average='weighted')))
    print("f1: {}".format(f1_score(true_value, pred,average='weighted')))
    


# Using GradientBoostingClassifier

classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=42)

# splitting data into training and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=2)



# build an over samled model with SMOTE and type as 'svm'
smote_pipeline = make_pipeline_imb(SMOTE(random_state=4,kind='svm'), classifier)
smote_model = smote_pipeline.fit(X_train, y_train)
smote_prediction = smote_model.predict(X_test)


#function to plot the confusion matrix

def plot_confusion_matrix(df_confusion, title='Confusion matrix', cmap=plt.cm.gray_r):
    plt.matshow(df_confusion, cmap=cmap) # imshow
    #plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(df_confusion.columns))
    plt.xticks(tick_marks, df_confusion.columns, rotation=0)
    plt.yticks(tick_marks, df_confusion.index)
    #plt.tight_layout()
    plt.ylabel(df_confusion.index.name)
    plt.xlabel(df_confusion.columns.name)

#call function to plot the confusion matrix
rating_label=['1','2','3','4','5']
print("Plot for Normal and SMOTE sample respectively")
plot_confusion_matrix(pd.DataFrame(confusion_matrix(y_test,smote_prediction),columns=rating_label))







