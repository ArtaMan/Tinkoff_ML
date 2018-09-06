import pickle
import random
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument('-m', '--model', action='store', dest='model', help='Файл модели')
    parser.add_argument('-s', '--seed', action='store', dest='seed', help='Сид')
    parser.add_argument('-l', '--length', action='store', dest='length', help='Длина текста')
    return parser.parse_args()

arguments = parse_args()
args = arguments.__dict__

model = args['model']
if 'seed' in args:
    seed = args['seed']
else:
    seed = 'в'
length = int(args['length'])


with open(model, 'rb') as f:
    data = pickle.load(f)
for i in range(length - 1):
    print(seed, end=' ')
    seed = random.choice(data[seed])