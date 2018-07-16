
class Presenter:
    def __init__(self, model):
        """
	    Initialization
	    @params
	        model = the model object to use to fetch appropriate data
	    return
	        N/A
        """
        self.model = model
    
    def home(self):
        return 'home.html'

    def getSites(self):
        return self.model.getSites()
    
    def getNoAnswerQuestions(self, site, minimum, maximum):
        return self.model.getNoAnswerQuestions(site, minimum, maximum)