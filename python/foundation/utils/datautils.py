class Nconfig:
    def __init__(self, **config_dict):
        for k,v in config_dict.items():
            if isinstance(v,dict):
                self.__dict__[k] = DictConfig(**v)
            else:
                self.__dict__[k] = v