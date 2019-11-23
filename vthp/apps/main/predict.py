import pandas as pd

def get_excel(file):
    df = pd.read_excel(file)
    index = df.index
    columns = df.columns

    omiss = df[ columns[-1] ]
    ftrs = []
    for i in range( len(index) ):
        ftrs.append( list( df.iloc[i, 1:( len(columns) - 1 )] ) )

    return ftrs, omiss

def match(predicted, omiss_p):
    k = 0
    e = 3
    for i in range( len(omiss_p) ):
        if ((predicted[i] + e) >= omiss_p[i]) \
       and ((predicted[i] - e) <= omiss_p[i]):
            k += 1

    return k

def predict(m, ftrs, ftrs_p, omiss, omiss_p):
    if m == 1:
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
    elif m == 2:
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
    elif m == 3:
        from sklearn.neighbors import KNeighborsClassifier
        model = KNeighborsClassifier()
    elif m == 4:
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    elif m == 5:
        from sklearn.svm import SVC
        model = SVC()

    model.fit(ftrs, omiss)
    predicted = model.predict(ftrs_p)

    return predicted
    #return match(predicted, omiss_p)

def main(excel, excel_p):
    ftrs, omiss = get_excel(excel)
    ftrs_p, omiss_p = get_excel(excel_p)

    #df = pd.DataFrame(df['ID'])

    df = pd.read_excel(excel_p)
    for m in range(5):
        df[str(m + 1)] = list(predict(m + 1, ftrs, ftrs_p, omiss, omiss_p))

    writer = pd.ExcelWriter("public/media/out.xls", engine='xlsxwriter')
    df.to_excel(writer, sheet_name = 'sheet1', index=False)
    writer.save()

if __name__ == '__main__':
    main('base/Пропуски_занятий.xls', 'base/Пропуски_занятий(copy).xls')
