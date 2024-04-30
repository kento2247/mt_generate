import json
import shutil

image_paths_dir = "images_list/"
output_folder = "trainset"
model_name = "grit"


def mkdir():
    import os

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"{output_folder} is created.")
    else:
        print(f"{output_folder} is already exists.")
    if not os.path.exists(f"{output_folder}/{model_name}"):
        os.makedirs(f"{output_folder}/{model_name}")
        print(f"{output_folder}/{model_name} is created.")
    else:
        print(f"{output_folder}/{model_name} is already exists.")


def main():
    image_paths = []
    used_image_ids = []
    with open(image_paths_dir + "all_images.txt", "r") as f:
        image_paths = f.read().splitlines()
    with open(f"config/{model_name}_coco_train.json", "r") as f:
        data = json.load(f)
        for d in data:
            used_image_ids.append(d["image_id"])

    for i in image_paths:
        image_id = i.split("_")[2].split(".")[0]
        image_id = int(image_id)
        # image_idがused_image_idsに含まれている場合は無視
        if image_id in used_image_ids:
            continue

        # trainset/{model_name}にtrain2014/{i}をコピー
        shutil.copy(f"train2014/{i}", f"{output_folder}/{model_name}/{i}")


if __name__ == "__main__":
    mkdir()
    main()
