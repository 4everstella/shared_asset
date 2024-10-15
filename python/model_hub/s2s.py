import os
import subprocess
import argparse

################################################################################
# utility
def check_file_path(file_path):
    print(f"Check: file - {file_path}")
    if not os.path.exists(file_path):
        print(f"Error: file is not existed - {file_path}")
        exit

def launch_cmd(cmd):
    print(" ".join(cmd))
    result = subprocess.run(cmd, capture_output = False, text = True)

################################################################################
def launch_asr(root_repo, i, o):
    #tool = "fasterwhisper_asr.py"
    tool = "funasr_asr.py"
    asr = os.path.join(root_repo, "tools", "asr", tool)
    s = "large"
    l = "zh"
    p = "float32"
    cmd = [
        "python", asr,
        "--input_folder",  i,
        "--output_folder", o,
        "--model_size",    s,
        "--language",      l,
        "--precision",     p
    ]
    launch_cmd(cmd)
    return    

def launch_tts(root_repo, text, output):
    tts = os.path.join(root_repo, "GPT_SoVITS", "inference_cli.py")
    gm = os.path.join(root_repo, "GPT_weights_v2", "cgn04-e15.ckpt")
    sm = os.path.join(root_repo, "SoVITS_weights_v2", "cgn04_e8_s208.pth")
    ra = "/mnt/data01/home/ycao/Downloads/audios/cgn/slice/CGN01.m4a_0000000000_0000141120.wav"
    rt = "乘客们列车马上就要"
    tt = text
    tl = "ZH"
    cmd = [
        "python", tts,
        "--gpt_model", gm,
        "--sovits_model", sm,
        "--ref_audio", ra,
        "--ref_text", rt,
        "--target_text", tt,
        "--target_language", tl,
        "--output_path", output
    ]
    launch_cmd(cmd)
    return

def main(args):
    root_gpt_sovits = args.root_gpt_sovits
    root_input      = args.root_input
    root_text       = args.root_text
    root_output     = args.root_output
    #launch_asr(root_gpt_sovits, root_input, root_text)
    file_text = os.path.join(root_text, "input.list")
    launch_tts(root_gpt_sovits, file_text, root_output)
    return

################################################################################
if __name__ == "__main__":
    _msg = "Speech to speech wapper of GPT-OVITS"
    dft_gpt_sovits_root = os.path.join("..", "..", "master")
    parser = argparse.ArgumentParser(description = _msg)
    parser.add_argument('root_gpt_sovits',
                        type = str,
                        help = "GPT-SoVITS repository root")
    parser.add_argument('root_input', type = str, help = "input speech file")
    parser.add_argument('root_text', type = str, help = "input speech file")
    parser.add_argument('root_output', type = str, help = "output speech file")
    parser.add_argument('-v', '--verbose',
                        action = 'store_true',
                        help = "Enable verbose mode")
    args = parser.parse_args()
    check_file_path(args.root_gpt_sovits)
    check_file_path(args.root_input)
    check_file_path(args.root_text)
    check_file_path(args.root_output)
    main(args)
