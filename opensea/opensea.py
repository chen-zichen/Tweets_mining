# for mining the data from opensea
# Retrieve collection stats

import pandas as pd
import requests
import json

def get_collection_stats(collection_slug, save_path):
    # get the data from the api
    url = "https://api.opensea.io/api/v1/collection/" + collection_slug + "/stats"

    # return the data
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.text

def import_slug(path):
    # import the slug from the csv file
    with open(path, 'r') as f:
        slug = f.read()
    # convert the slug to a list
    slug = slug.split(',\n')

    return slug

def save_data(data, save_path):
    # save the data to the path
    # save data dict to json file

    with open(save_path, 'a') as f:
        json.dump(data, f)
        f.write('\n')


if __name__ == "__main__":
    slug_path = "slug.csv"
    save_path = "collection_stats.jsonl"
    excel_path = "collection_stats.xlsx"

    slug_list = import_slug(slug_path)
    all_dict = {}
    for slug in range(len(slug_list)):
        stat = get_collection_stats(slug_list[slug], save_path)
        # convert str stat to dict
        stat = json.loads(stat)
        stat[slug_list[slug]] = stat['stats']
        del stat['stats']
        # print(stat)
        save_data(stat, save_path)
        all_dict.update(stat)
        print(slug_list[slug])
    # save to excel
    # change column and index 
    df = pd.DataFrame(all_dict).T
    df.to_excel(excel_path)

    