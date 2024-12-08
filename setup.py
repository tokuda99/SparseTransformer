#python3 setup.py install
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
from distutils.sysconfig import get_config_vars

(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)

setup(
    name='sptr',
    version="1.0.0",
    packages=find_packages(where="sptr"),
    package_dir={"": "sptr"}, 
    ext_modules=[
        CUDAExtension('sptr_cuda', [
            'src/sptr/pointops_api.cpp',
            'src/sptr/attention/attention_cuda.cpp',
            'src/sptr/attention/attention_cuda_kernel.cu',
            'src/sptr/precompute/precompute.cpp',
            'src/sptr/precompute/precompute_cuda_kernel.cu',
            'src/sptr/rpe/relative_pos_encoding_cuda.cpp',
            'src/sptr/rpe/relative_pos_encoding_cuda_kernel.cu',
            ],
        extra_compile_args={'cxx': ['-g', '-O3'], 'nvcc': ['-O3']}
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    python_requires='>=3.8',
)
