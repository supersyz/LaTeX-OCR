import PyInstaller.__main__
import os
import sys
import torch
import torchvision

def build_exe():
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取torch和torchvision的路径
    torch_path = os.path.dirname(torch.__file__)
    torchvision_path = os.path.dirname(torchvision.__file__)
    
    # PyInstaller参数
    args = [
        'launch_gui.py',  # 入口脚本
        '--name=LaTeX-OCR',  # 生成的exe名称
        '--onefile',  # 打包成单个文件
        '--noconsole',  # 不显示控制台窗口
        '--clean',
        # 添加数据文件
        '--add-data=pix2tex/model/checkpoints;pix2tex/model/checkpoints',  # 模型文件
        '--add-data=pix2tex/model/settings;pix2tex/model/settings',  # 配置文件
        f'--add-data={os.path.join(torch_path, "lib")};torch/lib',
        
        # 添加必要的导入
        '--hidden-import=PIL._tkinter_finder',
        '--hidden-import=pix2tex',
        '--hidden-import=timm',
        '--hidden-import=transformers',
        '--hidden-import=torch',
        '--hidden-import=torchvision',
        '--hidden-import=numpy',
        '--hidden-import=tkinter',
        '--hidden-import=pix2tex.gui',
        '--hidden-import=pix2tex.cli',
        '--hidden-import=torch._numpy',
        '--hidden-import=torch._numpy._ndarray',
        '--hidden-import=torch._numpy._dtypes',
        '--hidden-import=torch._numpy._dtypes_impl',
        '--hidden-import=torch._numpy._funcs',
        '--hidden-import=torch._numpy._ufuncs',
        '--hidden-import=torch._numpy._util',
        '--hidden-import=torch._dynamo',
        '--hidden-import=torch._dynamo.utils',
        '--hidden-import=torchvision.ops.roi_align',
        '--hidden-import=torchvision.models.feature_extraction',
        
        # 收集所有相关包
        '--collect-all=pix2tex',
        '--collect-all=timm',
        '--collect-all=transformers',
        '--collect-all=torch',
        '--collect-all=torchvision',
        

    ]
    
    PyInstaller.__main__.run(args)

if __name__ == '__main__':
    build_exe() 