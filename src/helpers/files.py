import pickle
import os


class Files:
    @staticmethod
    def save_obj(path, obj, name):
        with open(path + "/" + name + '.pkl', 'wb+') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_obj(path, name):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path +'/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)
