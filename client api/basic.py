import requests
endpoint= "http://127.0.0.1:8000/api/"
response=requests.get(endpoint,params={'abc':123}, json={'query':'hello'})
print(response.json())
print(response.status_code)

#HTTP Resquest-->HTML
#REST API HTTP -->JSON Javascipt Notation

