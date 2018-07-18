
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
    
    def getStackExchange(self):
        return ('stackexchange.html', self.getSites())

    def getSites(self):
        return self.model.getSites()
    
    def getNoAnswerQuestions(self, site):
        return ('stackexchange.html', self.model.getNoAnswerQuestions(site))