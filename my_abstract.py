from abc import ABCMeta, abstractmethod, abstractproperty

class Shape:
    __metaclass__ = ABCMeta
    @abstractmethod # built in to python
    def display(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass

