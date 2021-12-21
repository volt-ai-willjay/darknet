import os
os.environ['GPU_TYPE'] = str(os.popen('nvidia-smi --query-gpu=name --format=csv,noheader').read())

def getGPUArch(argument):
    try:
        argument = argument.strip()
        # All Colab GPUs
        archTypes = {
            "Tesla V100-SXM2-16GB": "-gencode arch=compute_70,code=[sm_70,compute_70]",
            "Tesla K80": "-gencode arch=compute_37,code=sm_37",
            "Tesla T4": "-gencode arch=compute_75,code=[sm_75,compute_75]",
            "Tesla P40": "-gencode arch=compute_61,code=sm_61",
            "Tesla P4": "-gencode arch=compute_61,code=sm_61",
            "Tesla P100-PCIE-16GB": "-gencode arch=compute_60,code=sm_60",
            "Quadro P4000": "-gencode arch=compute_75,code=[sm_75,compute_75]",
            "Quadro P5000": "-gencode arch=compute_75,code=[sm_75,compute_75]",
            "Quadro P6000": "-gencode arch=compute_75,code=[sm_75,compute_75]",
            "Quadro RTX 5000": "-gencode arch=compute_75,code=[sm_75,compute_75]",
            "Quadro RTX 4000": "-gencode arch=compute_75,code=[sm_75,compute_75]",
          }
        return archTypes[argument]
    except KeyError:
        return "GPU must be added to GPU Commands"
os.environ['ARCH_VALUE'] = getGPUArch(os.environ['GPU_TYPE'])

print("GPU Type: " + os.environ['GPU_TYPE'])
print("ARCH Value: " + os.environ['ARCH_VALUE'])


os.system("sed -i 's/OPENCV=0/OPENCV=1/g' Makefile")
os.system("sed -i 's/GPU=0/GPU=1/g' Makefile")
os.system("sed -i 's/CUDNN=0/CUDNN=1/g' Makefile")
os.system(f"sed -i \"s/ARCH= -gencode arch=compute_60,code=sm_60/ARCH= ${os.environ['ARCH_VALUE']}/g\" Makefile")
os.system("make")