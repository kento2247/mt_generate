# {"name": "grit", "len": 8721},
# {"name": "m2", "len": 7486},
# {"name": "git", "len": 9460},
# {"name": "sat", "len": 7790},
# {"name": "newton_gpt4v", "len": 7500},

# imagesの中のフォルダを、上記のメソッドごとに開き、lsでファイル名を取得。concatし、images.txtに書き込む
# images/images.txtを初期化
echo "" > images/images.txt
for i in grit m2 git sat newton_gpt4v
do
    echo $i
    ls images/$i >> images/images.txt
done

# images.txtを開いて、重複がないか確認
cat images/images.txt | sort | uniq -d