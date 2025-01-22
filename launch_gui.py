#!/usr/bin/env python
import os
import sys
import torch
import torchvision
from argparse import ArgumentParser

def main():
    # 确保所有必要的路径都被添加到sys.path
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # 设置环境变量
    os.environ['PYTHONPATH'] = application_path
    
    # 设置配置文件和模型文件的路径
    config_path = os.path.join(application_path, 'pix2tex', 'model', 'settings', 'config.yaml')
    checkpoint_path = os.path.join(application_path, 'pix2tex', 'model', 'checkpoints', 'weights.pth')
    
    parser = ArgumentParser()
    parser.add_argument('-t', '--temperature', type=float, default=.333, help='Softmax sampling frequency')
    parser.add_argument('-c', '--config', type=str, default=config_path, help='path to config file')
    parser.add_argument('-m', '--checkpoint', type=str, default=checkpoint_path, help='path to weights file')
    parser.add_argument('--no-cuda', action='store_true', help='Compute on CPU')
    parser.add_argument('--no-resize', action='store_true', help='Resize the image beforehand')
    parser.add_argument('--gui', action='store_true', default=True, help='Use GUI')
    arguments = parser.parse_args()

    try:
        from pix2tex.gui import main as gui_main
        gui_main(arguments)
    except Exception as e:
        import traceback
        with open('error_log.txt', 'w') as f:
            f.write(f"Error: {str(e)}\n")
            f.write(traceback.format_exc())
        raise

if __name__ == '__main__':
    main()