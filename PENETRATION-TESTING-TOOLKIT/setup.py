from setuptools import setup, find_packages

setup(
    name='pentest-toolkit',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A toolkit for penetration testing with multiple modules including a port scanner and brute forcer.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pentest-toolkit',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        # Add other dependencies here as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)