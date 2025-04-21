from setuptools import setup, find_packages

setup(
    name="SmartAITool",
    version="0.4.1",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        'opencv-python>=4.0.0',
        'tqdm>=4.0.0',
    ],
)
