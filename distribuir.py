from os import path, listdir
import pathlib
import random
import shutil

labels_folder = 'labels'
images_folder = 'images'
labels = [l for l in listdir(labels_folder) if l != '.gitkeep']
images = [i for i in listdir(images_folder) if i != '.gitkeep']
test_len = int(len(images) * 0.1)
train_len = int(len(images) * 0.9)
test = []
train = []
while len(test) != test_len:
  idx = random.randint(0, len(images) - 1)
  if not images[idx] in test:
    test.append(images[idx])
for i in images:
  if not i in test:
    train.append(i)
test_dest = 'dataset/valid'
train_dest = 'dataset/train'
print('test')
for t in test:
  label = pathlib.Path(t).stem + '.txt'
  shutil.copy(path.join(images_folder, t), f'{test_dest}/images')
  shutil.copy(path.join(labels_folder, label), f'{test_dest}/labels')
print('train')
for t in train:
  label = pathlib.Path(t).stem + '.txt'
  shutil.copy(path.join(images_folder, t), f'{train_dest}/images')
  shutil.copy(path.join(labels_folder, label), f'{train_dest}/labels')