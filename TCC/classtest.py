from sklearn import metrics
from sklearn.metrics import accuracy_score
import random
import ClassManager
import Process

p = Process.Process
c = ClassManager.SkTools


list = p.see_list()
limit = len(list)

if limit%2 != 0:
    limit -= 1

new_l = random.sample(list, len(list))
train = new_l[:(int((len(list))/2))]
test = new_l[(int((len(list))/2)):limit]

cls_x = [train[l][0] for l in range(len(train))]
cls_y = [test[l][0] for l in range(len(test))]
txt_x = [train[l][1][1] for l in range(len(train))]
txt_y = [test[l][1][1] for l in range(len(train))]

predict = c.to_classify(cls_x, txt_x, txt_y)
print(round((accuracy_score(cls_y, predict) * 100), 2), "\n\n",metrics.confusion_matrix(cls_y, predict))
