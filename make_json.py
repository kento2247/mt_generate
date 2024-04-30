import json


id_list_path = "images_list/old_all_images.txt"
output_folder = "configs/"
detasets = [
    {"name": "grit", "len": 8721},
    {"name": "m2", "len": 7486},
    {"name": "git", "len": 9460},
    {"name": "sat", "len": 7790},
    {"name": "newton_gpt4v", "len": 7500},
]


def make_json():
    # Read the id list
    with open(id_list_path, "r") as f:
        id_list = f.read().splitlines()
    row_num = 0
    for i in detasets:
        # 各dataset_idに対して{"image_id" = "12345", "caption" = ""}の要素を追加。先頭には"meta":{"begin":xxx, "end":xxx, "len":xxx}を追加
        dataset_name = i["name"]
        dataset_len = i["len"]
        output_file_name = f"{dataset_name}_coco_train.json"
        output_path = output_folder + output_file_name
        detaset_id_list = []
        # detaset_id_list.append({"meta":{"begin":row_num, "end":row_num+dataset_len, "len":dataset_len}})
        for j in range(dataset_len):
            image_file_name = id_list[row_num]
            image_id = image_file_name.split("_")[2]
            image_id = image_id.split(".")[0]
            image_id: int = int(image_id)
            detaset_id_list.append({"image_id": image_id, "caption": ""})
            row_num += 1
        with open(output_path, "w") as f:
            json.dump(detaset_id_list, f, indent=4)
        print(f"{output_file_name} is created.")


def main():
    make_json()


if __name__ == "__main__":
    main()
