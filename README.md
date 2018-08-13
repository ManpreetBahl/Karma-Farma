# Karma Farma
Copyright 2018 Manpreet Bahl

A Python Flask web application that helps to farm karma faster on both Stack Exchange and Reddit. 

For Stack Exchange, this application utilizes the Stack Exchange API to find recent questions with no answers, filters them based on view count and creation time of the post, and presents it to the user in a tabular fashion. This can be utilized on any of the sites on Stack Exchange.

For Reddit, this application utilizes PRAW (Python Reddit API Wrapper) to interact with the Reddit API. The application utilizes Reddit's OAuth for Authentication and for a more personalized experience. The application will fetch all of the authenticated user's subscribed subreddits in which the user will select one. The application will fetch the 100 newest posts in that selected subreddit and display the results in a tabular fashion.

It's important to note that this is a MVP (Minimal Viable Product). There are plans to enhance this application as detailed [here](#Future Work).

### Future Work
 

# License
Karma Farma is licensed under the MIT license. See the [LICENSE](LICENSE) for details.
