import requests
import json
from selenium import webdriver
import os


'''
get/movie/{movie_id}
get/movie/{movie_original_title}
https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US

https://api.themoviedb.org/3/discover/movie?api_key=<<api_key>>
&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1

https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>
&language=en-US&page=1&include_adult=false
'''
movie_id = 209112
# movie_id = 550
api_version = 3
api_base_url = "https://api.themoviedb.org/3"
# endpoint_path = f"/movie/{movie_id}"
endpoint_path = "/search/movie"
# query_data = "&language=en-US&query=superman&page=1"
query_data = "&language=en-US&query=superman&page="
endpoint = f"{api_base_url}{endpoint_path}?api_key={os.environ['api_key']}{query_data}"
# endpoint = f"{api_base_url}{endpoint_path}?api_key={os.environ['api_key']}"
print(endpoint)
epresponse = requests.get(endpoint)
print(epresponse.status_code)
# print(epresponse.text)
rdict = epresponse.json()
# print(rdict)
# new_string = json.dumps(rdict, indent=2, sort_keys=True)
print(rdict['total_pages'])
for x in range(1, int(rdict['total_pages'])+1):
    epresponse = requests.get(endpoint+str(x))
    newpage = epresponse.json()
    with open(f"C:\All_Projects\API_projects\TheMovieDBSearchSuperman{x}.json", "w") as superman:
        json.dump(newpage, superman, indent=2, sort_keys=True)
# new_string = json.dumps(rdict, indent=2)
# print(new_string)



# epresponse2 = requests.get(https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US)