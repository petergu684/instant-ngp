import json
import random
import shutil
from pathlib import Path
from tqdm import tqdm

ws_path = Path('/mnt/hdd1/slam_data/CadaverImages/WithPin/scene1')

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def split_images(num_image_per_folder = 50):
    image_path = ws_path / 'images'

    output_path = ws_path.parent / (ws_path.name + '_split_' + str(num_image_per_folder))
    output_path.mkdir(parents=True, exist_ok=True)

    # get all images
    all_image_names = list(image_path.glob('*.png'))
    num_images = len(all_image_names)
    print(f'Found {num_images} images')

    # shuffle images
    random.shuffle(all_image_names)

    images_names_chunks = list(chunks(all_image_names, num_image_per_folder))

    # copy images
    for i, chunk in tqdm(enumerate(images_names_chunks)):
        folder_name = f'{ws_path.name}_{i:03d}'
        dst_path = output_path / folder_name / 'images'
        dst_path.mkdir(parents=True, exist_ok=True)
        for image_name in chunk:

            src = image_path / image_name.name
            dst = dst_path / image_name.name

            # copy image
            shutil.copy(src, dst)


if __name__ == '__main__':
    # main()
    split_images(150)