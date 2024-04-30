import json


def main():
    captions = []
    image_files = []
    ignore_image_ids = []

    with open("config/git_coco_train.json", "r") as f:
        data = json.load(f)
        for d in data:
            ignore_image_ids.append(d["image_id"])

    with open("annotations/captions_train2014.json", "r") as f:
        data = json.load(f)
        annotations = data["annotations"]
        for a in annotations:
            # ignore_image_idsに含まれている場合は無視
            # 含まれていない場合は、captions,image_idsに追加
            if a["image_id"] in ignore_image_ids:
                continue
            captions.append(a["caption"])
            image_files.append(
                f"../mt_generate/train2014/COCO_train2014_{str(a['image_id']).zfill(12)}.jpg"
            )

    output_file = "config/git_pretrain_info.json"
    with open(output_file, "w") as f:
        json.dump({"captions": captions, "image_files": image_files}, f, indent=4)


if __name__ == "__main__":
    main()
