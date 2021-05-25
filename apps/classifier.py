import time
import numpy as np
import streamlit as st
import pickle as pk
import matplotlib.pyplot as plt
from scipy import stats
from apps.data import get_data
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class Classifier:
    def __init__(self):

        self.counter = 0

        with st.empty():
            st.write("⏳ Starting Engine...")

            if(self.__load_model()):
                # Show prediction fields
                st.info('✔️ Model loaded.')
                # p = self.knn.predict([[1, 0, 2018,    0,    0,    1,    3,   19,    0,    0,    3,    3,    7]])
                # st.info(p[0])
            else:
                # set model
                st.write('⏳ Loading data.')
                self.step()
                self.finance = get_data('data/inclusion.csv')

                # st.progress(self.counter)

                self.train()
            return



    def __load_model(self):
        with st.empty():
            st.write("⏳ Loading Model...")
            self.step()

            try:
                self.knn = pk.load(open('models/knn.pickle', 'rb'))
                return True
                # result = loaded_model.score(X_test, Y_test)
                # print(result)
            except IOError:
                st.write("❌ Model not found...")
                self.step()
                return False

    def step(self):
        if self.counter < 100:
            self.counter += 7
        else:
            self.counter = 100
        # st.progress(self.counter)
        time.sleep(0.5)
        return


    def __box_plots():
        fig, (ax1, ax2,ax3) = plt.subplots(3,1, figsize=(10,20))
        fig.suptitle('Outlier Detection')

        st.boxplot(finance['year'], ax= ax1, orient = 'v')
        st.boxplot(finance['age_of_respondent'],ax = ax2, orient = 'v')
        st.boxplot(finance['household_size'], ax = ax3, orient = 'v')

    def __clean_data(self):
        with st.empty():
            st.write("⏳ Dropping unwanted data...")
            self.step()
            self.finance = self.finance.drop(['uniqueid'], axis=1)

            st.write("⏳ Checking for outliers...")
            self.step()
            num = ['age_of_respondent', 'household_size']
            for i, col in enumerate(num):
                z = np.abs(stats.zscore(self.finance[col]))

            st.write("⏳ Dropping outliers using the Z score...")
            self.step()
            self.finance = self.finance[( z < 2 )]
            # self.finance2 = self.finance[( z < 2 )]

            st.write("⏳ Dropping values from the upper and lower quantiles...")
            self.step()
            Q1 = self.finance.quantile(0.25)
            Q3 = self.finance.quantile(0.75)
            IQR = Q3 - Q1

            self.finance3 = self.finance[~((self.finance < (Q1 - 1.5 * IQR)) |(self.finance > (Q3 + 1.5 * IQR))).any(axis=1)]

        # Plot box plots
        # self.__box_plots()
        return

    def __plot_correlation_matrix():
        with st.empty():
            st.write("⏳ Finding correlations...")
            self.step()
            corrMatrix = self.finance.corr()
            fig, ax = plt.subplots(figsize=(10,10))

            st.write("⏳ Plotting heatmap...")
            self.step()
            st.heatmap(corrMatrix, annot=True,  linewidths=.5, ax=ax)
            st.empty()
        return

    def __encode(self):
        # Encode categorical data into numerical data
        with st.empty():
            st.write("⏳ Encoding data...")
            self.step()
            en = LabelEncoder()
            self.finance['country'] = en.fit_transform(self.finance['country'])
            self.finance['bank_account'] = en.fit_transform(self.finance['bank_account'])
            self.finance['location_type'] = en.fit_transform(self.finance['location_type'])
            self.finance['cellphone_access'] = en.fit_transform(self.finance['cellphone_access'])
            self.finance['gender_of_respondent'] = en.fit_transform(self.finance['gender_of_respondent'])
            self.finance['relationship_with_head'] = en.fit_transform(self.finance['relationship_with_head'])
            self.finance['marital_status'] = en.fit_transform(self.finance['marital_status'])
            self.finance['education_level'] = en.fit_transform(self.finance['education_level'])
            self.finance['job_type'] = en.fit_transform(self.finance['job_type'])
            st.empty()

        # Plot correlation heatmap
        # self.__plot_correlation_matrix()
        return

    def __accuracy_plot(k_range, scores_list):
        with st.empty():
            st.write("⏳ Plotting scores.")
            self.step()
            plt.plot(k_range,scores_list)
            plt.xlabel('Value of K for KNN')
            plt.ylabel('Testing Accuracy')
            st.empty()
        return

    def __write_to_disk(self):
        with st.empty():
            st.write("⏳ Saving model...")
            filename = 'models/knn.pickle'
            pk.dump(self.knn, open(filename, 'wb'))
            st.info('✔️ Model saved.')
            return

    def train(self):
        self.__clean_data()
        self.__encode()

        finance = self.finance

        with st.empty():
            st.write("⏳ Generating response vector...")
            self.step()
            y = finance.bank_account

            finance = finance.drop(['bank_account', 'Unnamed: 0'], axis=1)

            st.write("⏳ Generating feature matrix...")
            self.step()
            X = finance.to_numpy()

            st.write("⏳ Generating training and testing sets...")
            self.step()

            # splitting the data into training and test sets (80:20)
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

            st.write("⏳ Training model, please be patient.")

            #Try running from k=1 through 25 and record testing accuracy
            k_range = range(1,25)
            scores = {}
            scores_list = []
            for k in k_range:
                knn = KNeighborsClassifier(n_neighbors=k)
                knn.fit(X_train,y_train)
                y_pred=knn.predict(X_test,)
                scores[k] = metrics.accuracy_score(y_test,y_pred)
                scores_list.append(metrics.accuracy_score(y_test,y_pred))

            self.knn = knn
            st.write("✔️ Training Complete.")
            self.step()
            st.empty()
            self.__write_to_disk()

            # self.__accuracy_plot(k_range, scores_list)
        return

    def predict(self, arr):
        # words = [
        #     "⏳ Generating prediction...",
        #     "🔮 Working magic ...",
        #     "⏳ Working response vector..."
        # ]

        with st.empty():
            # st.info(words[random.randrange(0, 2)])
            st.info("⏳ Working response vector...")

            return self.knn.predict(arr)


