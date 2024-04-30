import numpy as np

input_dir = "images_list/"
input_file = "all_images_list.txt"
output_dir = "images_list/"
output_file = input_file.split(".")[0] + ".npy"

with open(input_dir + input_file, "r") as f:
    images_list = f.readlines()

images_list = [i.strip() for i in images_list]
images_list = np.array(images_list)
np.save(output_dir + output_file, images_list)
