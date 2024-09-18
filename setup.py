from setuptools import setup, find_packages

setup(
    name='qsimpy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21',  # Add any other dependencies here
        # Other libraries if necessary
    ],
    author='Suhas P K',
    author_email='sparrowjack0682@gmail.com',
    description='A quantum simulator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SuhasPK/qsimpy',  # Link to your project repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
