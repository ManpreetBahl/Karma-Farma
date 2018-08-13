"""
Copyright 2018 Manpreet Bahl
[This program is licensed under the "MIT License"]
Please see the file LICENSE in the source distribution 
of this software for license terms.
"""
from abc import ABC, abstractmethod

class IModel(ABC):

    @abstractmethod
    def getSites(self):
        pass
    
    @abstractmethod
    def getNoAnswerQuestions(self, site):
        pass