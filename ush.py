import os
import random
import shutil

# Paths
images_path "
labels_path = "Users\nagar\dataset\labels"

train_images_path = "Users\nagar\dataset\images\train"
val_images_path = "Users\nagar\dataset\images\val"
train_labels_path = "Users\nagar\dataset\labels\train"
val_labels_path = "Users\nagar\dataset\labels\val"

images = os.listdir(images_path)
random.shuffle(images)

# Split into train and val
train_size = int(0.8 * len(images))  # 80% for train
train_images = images[:train_size]
val_images = images[train_size:]

# Move images and labels to respective folders
for image in train_images:
    shutil.move(os.path.join("Users\nagar\dataset\images", image), os.path.join('Users\nagar\\dataset\\images\train'
, image))
    label_file = image.replace(".jpg", ".txt").replace(".png", ".txt")
    shutil.move(os.path.join("Users\nagar\\dataset\\labels", label_file), os.path.join('Users\nagar\\dataset\\labels\train', label_file))

for image in val_images:
    shutil.move(os.path.join("Users\nagar\dataset\images", image), os.path.join('Users\nagar\\dataset\\images\x0bal'
, image))
    label_file = image.replace(".jpg", ".txt").replace(".png", ".txt")
    shutil.move(os.path.join("Users\nagar\dataset\images"), label_file), os.path.join('Users\nagar\\dataset\\labels\x0bal', label_file))
