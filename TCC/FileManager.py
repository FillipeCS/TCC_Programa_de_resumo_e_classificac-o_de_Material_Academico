import pickle
import os
from multipledispatch import dispatch

sd = "subjectdata.dat"
sl = "subjectlist.dat"

class PTools():
#TOOLS
    def see_file(fl):
        try:
            with open(fl) as f:
                f.close()
        except IOError:
            with open(fl, 'wb') as f:
                pickle.dump([], f)
                f.close()

    def get_file(fl):
        data = {}
        if os.path.getsize(fl) > 0:
            with open(fl, "rb") as f:
                unpickler = pickle.Unpickler(f)
                data = unpickler.load()
        return data

    def save_file(fl, dt):
        with open(fl, 'wb') as f:
            pickle.dump(dt, f)
            f.close()

#COMMANDS
    def get_data(fl):
        PTools.see_file(fl)
        data = PTools.get_file(fl)
        return data

    @dispatch(str, str)
    def to_save_file(fl, dt):
        list = PTools.get_data(fl)
        if list != []:
            if dt not in list:
                list.append(dt)
        else:
            list.append(dt)
        PTools.save_file(fl, list)

    @dispatch(str, list)
    def to_save_file(fl, dt):
        list = PTools.get_data(fl)
        list_s = []
        list.append(dt)
        for l in list:
            if l not in list_s:
                list_s.append(l)
        PTools.save_file(fl, list_s)

    def file_manager(nm, tlt, txt):
        PTools.to_save_file(sd, nm)
        PTools.to_save_file(sl, [nm, [tlt, txt]])

    def file_deletion(lst):
        the_list = PTools.get_sub_list()
        del_list = []
        for l in the_list:
            if l != lst:
                del_list.append(l)
        PTools.save_file(sl, del_list)

    def get_sub_list():
        return PTools.get_data(sl)

    def get_sub_data():
        return PTools.get_data(sd)
