from setuptools import setup, find_packages

setup(
    name='prime-rack-1531',
    version='0.3.15',
    packages=find_packages(),
    install_requires=['requests>=2.28.0', 'click>=8.0'],
    entry_points={'console_scripts': ['prime-rack-1531=primerack:main']},
)
