import pickle
import argparse
import os
import re

def parse_args():
    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument('-d', '--dir', action='store', dest='dir', help='Папка с файлами')
    parser.add_argument('-m', '--model', action='store', dest='model', help='Файл модели')
    return parser.parse_args()

arguments = parse_args()
args = arguments.__dict__

dir = args['dir']
if dir[-1] != '/':
    dir = dir +  '/'
model = args['model']

files = os.listdir(dir)
main = {}
for i in range(len(files)):
    with open(dir + files[i]) as f:
        a = f.read().lower()
        clear = re.sub(u"[^а-я0-9\-\s]", "", a).split()
        for i in range(len(clear) - 1):
            if clear[i] not in main:
                main[clear[i]] = [clear[i + 1]]
            else:
                if clear[i + 1] not in main[clear[i]]:
                    main[clear[i]].append(clear[i + 1])
with open(model, 'wb') as f:
    pickle.dump(main, f)