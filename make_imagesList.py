import json

methods = ["git", "m2", "grit", "sat"]


def main():
    for method in methods:
        ignore_image_ids = []
        # config/git_coco_train.jsonを読み込む
        with open(f"config/{method}_coco_train.json") as f:
            config = json.load(f)
            for i in config:
                image_id = i["image_id"]
                ignore_image_ids.append(image_id)
        # images_list/{method}_images_list.txtに書き込む
        with open(f"images_list/{method}_images_list.txt", "w") as f:
            for image_id in ignore_image_ids:
                f.write(f"{image_id}\n")


if __name__ == "__main__":
    main()
