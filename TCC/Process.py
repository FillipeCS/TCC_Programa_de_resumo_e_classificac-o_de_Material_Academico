import TextManager
import ClassManager
import FileManager
import heapq
import string
import random

tm = TextManager.NTools
sk = ClassManager.SkTools
fm = FileManager.PTools

class Process():

    def summary(nm, txt):
        text_tk = tm.get_cleantoken(txt.lower())
        list = Process.get_text(nm)

        if list != []:
            text_tk = Process.get_all_tk(text_tk, list)

        sent_tk = tm.tokenizer_sent(txt)
        freq = tm.set_frequency(text_tk)
        sent_sc = tm.get_scoresent(sent_tk, freq)

        sum_sentences = heapq.nlargest(int((len(sent_tk)/2) - 1), sent_sc, key = sent_sc.get)
        sum = ' '.join(sum_sentences)

        return sum

    def classfy(txt):
        lst = fm.get_sub_list()
        if (lst == []):
            return None
        else:
            list = random.sample(lst, len(lst))
            list_text = []
            list_class = []
            for l in range(len(list)):
                list_class.append(list[l][0])
                list_text.append(str(list[l][1][1]).lower())
            predict = sk.to_classify(list_class, list_text, [str(txt).lower()])
            return predict

    def get_text(nm):
        list = fm.get_sub_list()
        subject_list = []
        for i in range(len(list)):
            if nm in list[i][0]:
                subject_list.append(list[i][1])
        return subject_list

    def get_all_tk(tk, lst):
        for l in range(len(lst)):
            for t in tm.get_cleantoken(lst[l][1].lower()):
                if t in tk:
                    tk.append(t)
        return tk

    def to_add_data(sb ,tt ,txt):
        try:
            e = Process.summary(sb, txt)
            fm.file_manager(sb ,tt ,txt)
            print("|operação concluida|")
        except IOError:
            input("\n[ERROR]\n|Texto não pode ser usado|\n\nAperte (ENTER) para continuar")

    def to_delete_data(lst):
        fm.file_deletion(lst)
        print("|operação concluida|")

    def see_file():
        return fm.get_sub_data()

    def see_list():
        return fm.get_sub_list()
