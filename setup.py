"""
Setup configuration for video_downloader_prod
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='video-downloader-prod',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Production-ready video segment downloader and converter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/video_downloader_prod',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Video',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests>=2.31.0',
        'tqdm>=4.66.0',
    ],
    entry_points={
        'console_scripts': [
            'video-downloader=main:main',
        ],
    },
)
