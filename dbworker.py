import json

def write_to_json(id, key, value):
    if ready(id):
        with open('data.json','r') as jfr:
            jf_file = json.load(jfr)
        with open('data.json','w') as jf:
            jf_target = jf_file[0]['users'][]
            user_info = {'name': name, 'date': date, 'city': city}
            jf_target.append(user_info)
            json.dump(jf_file, jf, indent=4)

def read_from_json(id):
    with open('data.json','r') as jfr:
        jf_file = json.load(jfr)

def ready(id):
    with open('data.json','r') as js:
        for car in json.loads(js)['cars']:
            if car['plate'] == plate:
                return true
        else:
            return false
