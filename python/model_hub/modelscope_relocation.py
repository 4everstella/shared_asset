import argparse
from modelscope import snapshot_download
import shutil
import os

def copy_item(src, dst):
    print(f"Processing - {src}")
    if os.path.isdir(src):
        if not os.path.exists(dst):
            shutil.copytree(src, dst)
    elif os.path.isfile(src):
        shutil.copy(src, dst)
    return

def download_model(model_id, destination_dir):
    local_dir = snapshot_download(model_id)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    for item in os.listdir(local_dir):
        item_path = os.path.join(local_dir, item)
        destination_path = os.path.join(destination_dir, item)
        copy_item(item_path, destination_path)
    return

if __name__ == "__main__":
    _msg = "Download and copy a ModelScope model with readable names."
    parser = argparse.ArgumentParser(description = _msg)
    parser.add_argument("model_id",
                        type = str,
                        help = "The ModelScope model ID (e.g., 'bert-base-uncased').")
    parser.add_argument("destination_dir",
                        type = str,
                        help = "The destination directory to copy the model files.")
    args = parser.parse_args()
    download_model(args.model_id, args.destination_dir)

