import json

dataset_path = "E:\data\caption_datasets"
dataset_name = "dataset_coco.json"

def read_dataset_json():
    f = open(dataset_path+dataset_name,'r')
    content = f.read()
    a = json.loads(content)
    print(type(a))
    print(a)
    f.close



read_dataset_json()