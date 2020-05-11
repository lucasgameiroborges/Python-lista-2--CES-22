import abc

class Lutador:
    __metaclass__ = abc.ABCMeta

    default_expertise = ['auto-defesa']

    @classmethod
    @abc.abstractmethod
    def get_expertise(cls):
        """"retorna o conhecimento do lutador"""
        return cls.default_expertise

    @abc.abstractmethod
    def get_estilo(self):
        """" retorna estilo de luta preferido"""

class Judoca(Lutador):
    def get_expertise(self):
        return ['koshiguruma', 'osotogari', 'kataguruma'] + super(Judoca, self).get_expertise()

    @staticmethod
    def get_estilo():
        return "Judo"


