import pickle


class Files:
    @staticmethod
    def save_obj(path, obj, name):
        with open(path + "/" + name + '.pkl', 'wb+') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_obj(path, name):
        with open(path +'/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)
