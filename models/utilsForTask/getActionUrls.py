import requests
import json
from datetime import datetime, date
# from prettytable import PrettyTable
# key =AIzaSyBSr7dCqLcbRLwl83KzJJxstFqq7oeozgc
# for j in search("Kreator3d", tld="com", lang="en", num=5, start=0, stop=10, pause=2.0):
#     print(j)
#     print(type(j))


# x = requests.get(
#     "https://www.googleapis.com/customsearch/v1?key=AIzaSyBSr7dCqLcbRLwl83KzJJxstFqq7oeozgc&cx=2433b138511bfd41b&q=kreator&num=10")
# for i in x:
#     # i.decode('utf8').replace("'", '"')
#     # print(type(i))
#     # data = json.loads(i)
#     # s = json.dumps(data, indent=4, sort_keys=true)
#     # print(s)
#     print(json.loads(i))
from googleapiclient.discovery import build

my_api_key = "AIzaSyBSr7dCqLcbRLwl83KzJJxstFqq7oeozgc"  # The API_KEY you acquired
my_cse_id = "2433b138511bfd41b"  # The search-engine-ID you created


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    print(type(res['items']))
    return res['items']


def filteredResultMethod(search_terms):
    search_terms += "steps to "+search_terms
    results = google_search(
        search_terms, my_api_key, my_cse_id, num=10)
    filteredResults = {'Title': [], 'Channel': [], 'Link': []}
    for result in results:
        filteredResults['Title'].append(result['title'])
        filteredResults['Link'].append(result['link'])
        if 'youtube.com' in result['link']:
            print(result['link'])
            filteredResults['Channel'].append(
                result['pagemap']['person'][0]['name'])
        else:
            filteredResults['Channel'].append("Not a youtube Link")

    return filteredResults


#urlsToSend = filteredResultMethod()


def tableDisplay():
    table = PrettyTable()
    for key in urlsToSend:
        table.add_column(key, urlsToSend[key])
    print(table)
