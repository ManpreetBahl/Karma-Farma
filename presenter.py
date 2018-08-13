"""
Copyright 2018 Manpreet Bahl
[This program is licensed under the "MIT License"]
Please see the file LICENSE in the source distribution 
of this software for license terms.
"""
#====================Presenter========================
class Presenter:
    """
    This class defines the Presenter class in the MVP
    design. This class provides methods that interact
    with the model and specifies which view to render
    with the data.
    """
    def __init__(self, model):
        """
	    Initialization of the Presenter class

	    Parameters:
	        model: Model object to use to fetch appropriate data
        """
        self.model = model
    
    def home(self):
        """
        Specify the view for the home page

        Returns:
            String specifying name of the Home page
        """
        return 'home.html'
    
    #==================Stack Exchange======================
    def getStackExchange(self):
        """
        Specify the view for the Stack Exchange page

        Returns:
            String specifying name of the Stack Exchange page
        """
        return 'stackexchange.html'

    def getSites(self):
        """
        This method retrieves the sites on Stack Exchange 
        by calling the appropriate method in the model.

        Returns:
            List containing the sites on Stack Exchange
        """
        return self.model.getSites()
    
    def getNoAnswerQuestions(self, site):
        """
        This method retrieves questions with no answers
        by calling the appropriate method in the model.

        Returns:
            Tuple containing the view to render and
            the lists of questions with no answers by
            the model.
        """
        return ('stackexchange.html', self.model.getNoAnswerQuestions(site))
    #======================================================

    #=====================Reddit===========================
    def userApproveApp(self):
        """
        This method provides the OAuth URL for Reddit.

        Returns:
            OAuth URL as a string
        """
        return self.model.userApproveApp()
    
    def getUserSubreddits(self, code):
        """
        This method retrieves the authenticated user's
        subscribed subreddits.

        Parameters:
            code: The authenticated user, if not
                  authenticated already.
        
        Returns:
            List of user's subscribed subreddits
        """
        return self.model.getUserSubreddits(code)
    
    def getSubredditNew(self, sr):
        """
        This method retrieves the newest posts on 
        the specified subreddit.

        Parameters:
            sr = The subreddit to get new posts from
        
        Returns:
            List of newest posts. 
        """
        return self.model.getSubredditNew(sr)
    #======================================================
#=====================================================