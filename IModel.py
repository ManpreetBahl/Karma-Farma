from abc import ABC, abstractmethod

class IModel(ABC):

    @abstractmethod
    def getSites(self):
        pass
    
    @abstractmethod
    def getNoAnswerQuestions(self, site, min, max):
        pass