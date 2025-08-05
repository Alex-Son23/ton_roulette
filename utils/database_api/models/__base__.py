from utils.database_api import db_gino


class MyBaseModel(db_gino.Model):
    def __repr__(self):
        items = ''
        for i in self.__class__.__namespace__:
            if i[:2] != '__' and i[-2:] != '__':
                if isinstance(self.__getattribute__(i), str):
                    items += f"{i}='{self.__getattribute__(i)}', "
                else:
                    items += f"{i}={self.__getattribute__(i)}, "
        items = items[:-2]
        class_name = self.__class__.__name__
        return f'<{class_name}({items})>'
