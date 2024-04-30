import json


json_folder = "config/"
images_path = "images/"
detasets = [
    {"name": "grit", "len": 8721},
    {"name": "m2", "len": 7486},
    {"name": "git", "len": 9460},
    {"name": "sat", "len": 7790},
    {"name": "newton_gpt4v", "len": 7500},
]


def make_dir():
    import os

    # output_folder/detasets.nameが存在しない場合は作成
    for i in detasets:
        dataset_name = i["name"]
        output_path = images_path + dataset_name
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"{output_path} is created.")
        else:
            print(f"{output_path} is already exists.")


def mv_images():
    # {json_folder}/{detasets.name}_coco_train.jsonを開く
    # json内の各要素のimage_idに対応する画像をtrain2014からimages/detasets.nameに移動
    for i in detasets:
        dataset_name = i["name"]
        json_path = json_folder + dataset_name + "_coco_train.json"
        with open(json_path, "r") as f:
            json_data = json.load(f)
        for j in json_data:
            image_id = j["image_id"]
            image_file_name = f"COCO_train2014_{str(image_id).zfill(12)}.jpg"
            image_path = "train2014/" + image_file_name
            output_path = images_path + "/" + dataset_name + "/" + image_file_name
            import shutil

            shutil.move(image_path, output_path)
            print(f"{image_file_name} is moved to {output_path}.")


def main():
    make_dir()
    mv_images()


if __name__ == "__main__":
    main()
