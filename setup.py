import os 
from distutils.sysconfig import *
from setuptools import setup, Extension

pyUniDOE_module=Extension('_pyunidoe_swig', sources=['pyunidoe/pyunidoe_swig_wrap.cxx','pyunidoe/wrapper.cpp','pyunidoe/doe_optimizer.cpp','pyunidoe/doe_criteria.cpp',
                                'pyunidoe/doe_CD2.cpp','pyunidoe/doe_MD2.cpp','pyunidoe/doe_WD2.cpp', 
                                'pyunidoe/doe_maximin.cpp','pyunidoe/doe_MC.cpp','pyunidoe/doe_A2.cpp'])

setup(name='pyunidoe',
      version='0.1',
      description='Efficient procedures for constructing uniform design of experiments under various space-filling criteria. It is based on a stochastic and adaptive threshold accepting algorithm with flexible initialization, adaptive threshold, and stochastic evolution. The package may also construct the augmented uniform designs in a sequential manner.',
      author='Zebin Yang',
      author_email='yangzb2010@hku.hk',
      license='GPL',
      packages=['pyunidoe'],
      ext_modules=[pyUniDOE_module],
      package_dir = {'pyunidoe': 'pyunidoe'},
      package_data = {'pyunidoe': ['data/*.json']},
      install_requires=['matplotlib', 'numpy', 'pandas', 'seaborn'], zip_safe=False)