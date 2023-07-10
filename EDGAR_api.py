# Get links from SEC api calls and then scrape teh links for relevant data
from sec_api import QueryApi
import requests
import prompts
import json

# API endpoint
url = "https://api.sec-api.io/extractor"
# Read the API key from the config file
auth="" # ENTER AUTH KEY FOR EDGAR API

ten_k_items = prompts.ten_k_items

ten_q_items = prompts.ten_q_items

eight_k_items = prompts.eight_k_items

def get_item_number(filing_type, item_name):
    item_name = item_name
    filing_type = filing_type
    item_dict ={}

    if filing_type == '10-K':
        item_dict = ten_k_items
    elif filing_type == '10-Q':
        item_dict = ten_q_items
    elif filing_type == '8-K':
        item_dict = eight_k_items
    else:
        return 'Invalid filing type'

    print(f"Item name {item_name}")
    print(f"filing type {filing_type}")
    print(item_dict.get(item_name))
    if any(char.isdigit() for char in item_name): # if the item name is already a alphanum id 
        return item_name
    return item_dict.get(item_name, 'Invalid item type')

def get_financial_filings_urls(name,auth):
    queryApi = QueryApi(api_key=auth)
    filings_dict = {}

    # List of form types to query
    form_types = ["8-K", "10-Q", "10-K"]

    for form_type in form_types:
        query = {
            "query": {
                "query_string": {
                    "query": f"(formType:\"{form_type}\") AND companyName:{name}",
                }
            },
            "from": "0",
            "size": "1",  # Only fetch the latest document of the type
            "sort": [{"filedAt": {"order": "desc"}}]
        }

        response = queryApi.get_filings(query)

        if response["filings"]:
            filing = response["filings"][0]
            url = filing["linkToTxt"]
            filings_dict[form_type] = url

    return filings_dict
    #get company info with query api, return dictionary with newest link for all forms which will be passed to retrieve section

def retrieveSection(url, itemType, auth) -> str:
    # Request parameters
    params = {
        "url": url,
        "item": itemType,
        "type": "text",
        "token": auth
    }
    # Send request
    response = requests.get("https://api.sec-api.io/extractor", params=params)
    data = response.text

    return data
    
def run_sec_API(companyName, Form, Section):
    # Parameters above are what PALM returns
    urls = get_financial_filings_urls(companyName, auth)
    print(urls)
    data = retrieveSection(urls[Form],get_item_number(Form, Section), auth)
    print(data)


    return data