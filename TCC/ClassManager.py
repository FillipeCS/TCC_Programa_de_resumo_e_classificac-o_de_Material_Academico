from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

cvec = CountVectorizer()
tvec = TfidfTransformer()

class SkTools():
#TOOLS
    def vectorize_lst(lst):
        vectxt = cvec.fit_transform(lst)
        return vectxt

    def vectorize_txt(txt):
        vectxt = cvec.transform(txt)
        return vectxt

    def transform_matrix_lst(lst):
        tfidtxt= tvec.fit_transform(SkTools.vectorize_lst(lst))
        return tfidtxt

    def transform_matrix_txt(txt):
        tfidtxt= tvec.transform(SkTools.vectorize_txt(txt))
        return tfidtxt

    def classify_txt(lst, clss):
        classfy = MultinomialNB().fit(lst, clss)
        return classfy

#COMMANDS
    def to_classify(clss, lst, txt):
        list = SkTools.transform_matrix_lst(lst)
        text = SkTools.transform_matrix_txt(txt)
        clf = SkTools.classify_txt(list, clss)
        predict = clf.predict(text)
        return predict
