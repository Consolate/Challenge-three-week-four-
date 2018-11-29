import click
import requests

apikey=  'ced42af865c5482aa78652be689b4af0'

# four news sources 
def newsFromBBC():
    #news from bbc
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=ced42af865c5482aa78652be689b4af0"
    #main_url = "https://newsapi.org/v2/top-headlines?sources=associated-press&apiKey=ced42af865c5482aa78652be689b4af0"
    #main_url = "https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=ced42af865c5482aa78652be689b4af0"
    #main_url = "https://newsapi.org/v2/top-headlines?sources=focus&apiKey=ced42af865c5482aa78652be689b4af0"
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i])                  
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    newsFromBBC()  