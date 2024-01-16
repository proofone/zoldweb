import json



def import_ukh_gmap_json(fpath):
    with open(fpath, encoding='utf-8') as jf:
        json_data = json.loads(jf.read())
        members_data = json_data[1][6][0][12][0][13][0]
        for member_data in members_data:
            print(member_data[5][0][1])

def main():
    return import_ukh_gmap_json("./data/ukh_gmap_data.json")


if __name__ == '__main__':
    main()
