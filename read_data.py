import json
from collections import Counter



dataset_path = "E:/data/caption_datasets/"
dataset_name = "dataset_coco.json"

train_path = []#restval
test_path = []
val_path = []
train_tokes = []
test_tokes = []
val_tokes = []
words_count = Counter()

def read_dataset_json():
    f = open(dataset_path+dataset_name,'r')
    content = f.read()
    json_dic = json.loads(content)

    for i in range(len(json_dic["images"])):
        image = json_dic["images"][i]
        alist = []
        if image['split']=='train' or image['split']=='restval':
            train_path.append(image['filepath'] + '/' + image['filename'])
            for j in range(len(image['sentences'])):
                alist.append(image['sentences'][j]['tokens'])
            train_tokes.append(alist)
        elif image['split'] == 'test':
            test_path.append(image['filepath'] + '/' + image['filename'])
            for j in range(len(image['sentences'])):
                alist.append(image['sentences'][j]['tokens'])
            test_tokes.append(alist)
        else:
            val_path.append(image['filepath'] + '/' +image['filename'])
            for j in range(len(image['sentences'])):
                alist.append(image['sentences'][j]['tokens'])
            val_tokes.append(alist)
        for k in range(len(alist)):
            words_count.update(alist[k])

    return words_count

def set_wordmap():
    words = [w for w in words_count.keys()]
    word_map = {k: v + 1 for v, k in enumerate(words)}
    word_map['<unk>'] = len(word_map)+1
    word_map['<start'] = len(word_map)+1
    word_map['<end>'] = len(word_map)+1
    word_map['<pad>'] = 0
    with open("E:\data\mycaption_data\show_attention_tell\wordmap.json", "w") as f:
        json.dump(word_map, f)
    print("写文件完成...")


read_dataset_json()
set_wordmap()