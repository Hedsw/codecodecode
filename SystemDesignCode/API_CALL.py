# *limited internet access allowed for documentation purposes only*
# * Important documentation: https://docs.github.com/en/rest/repos/repos#list-organization-repositories *

# Task: Write code using python to hit a REST api endpoint `https://github.com/octokit`.
# Task: You may also use shell script to come to the same conclusion.
# Task: Get the list of repositories in the Octokit (https://github.com/octokit) organization sorted by number of stars, descending.
# Task: What things would you implement in your code to make it production ready?
# Task: Can you do it using an object oriented approach?

# Output should look like this:

# repo: octokit.js, num_of_stars: 5458
# repo: octokit.rb, num_of_stars: 3594
# etc etc

# First Approach 
# Query the URL such as below.. 
"""
For Sorted by number of Start and Descending, we could implement simply using Query such as
url = 'https://api.github.com/orgs/octokit/repos?q=sort=stargazers_count&order=descending'

After that, put the URL into the class and without dictionry, just print the name and stargazers_count 

However, I think this coding interview is combined usage of data structure and usage APIs so I implement second approach. 

Second approach use dictionray and sorted the dictionry ordered by number of stars.
Detail code is described below.

I used template method pattern to implement this code to extend this code for the future.
"""
import requests, json
from abc import ABC, abstractmethod

# First Approach
class callGithubRepo:
    def __init__(self, url):
        #self.repoName = repoName
        self.urls = []
        self.url = url
        self._dict = {}
    def execute(self):
        try: # Exception Handling 
            response = requests.get(self.url)
            if response.status_code != '200':
                text = response.text
                data = json.loads(text)
                
                for i in data:
                    self._dict[i['name']] = i['stargazers_count']
                
                _sortedDict = sorted(self._dict.items(), key = lambda x:x[1], reverse=True)
                for i in _sortedDict:
                    print("Repo: ", i[0], ", Number of Stars:", i[1])
        
            else: # Different Status Code
                print("URL Issue")
        except OSError as err: 
            print("OS ERROR: {0}".format(err))
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

url = 'https://api.github.com/orgs/octokit/repos'
obj = callGithubRepo(url)
obj.execute()
    