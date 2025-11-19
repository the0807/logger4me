from setuptools import setup, find_packages

setup(
    name='logger4me',
    version='0.0.2',
    description='A simple and colorful Python logging utility',
    author='the0807',
    author_email='the0807.eom@gmail.com',
    url='https://github.com/the0807/logger4me',
    license='MIT',
    packages=find_packages(exclude=[]),
    keywords = ["python", "logging", "color", "console", "utility", "ansi"],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
)
