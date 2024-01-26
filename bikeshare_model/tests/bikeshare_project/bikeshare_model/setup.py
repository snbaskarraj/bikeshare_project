# bikeshare_model/setup.py
# bikeshare_model/setup.py
from setuptools import setup, find_packages

setup(
    name="bikeshare_model",
    version="0.1.0",  # Consider automating version updates with a tool like bumpversion
    author="snbaskarraj",
    author_email="snbaskar@gmail.com",
    description="A model for predicting bikeshare usage patterns",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/snbaskarraj/bikeshare_project",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'numpy==1.23.2',   # or use a range like 'numpy>=1.21.0,<2.0.0',
        'pandas>=1.3.5,<2.0.0',
        'pydantic>=1.8.1,<2.0.0',
        'scikit-learn==1.3.0',
        'strictyaml>=1.3.2,<2.0.0',
        'ruamel.yaml>=0.16.12,<1.0.0',
        'joblib>=1.0.1,<2.0.0',
        'pytest>=6.0.0,<7.0.0',
        'black==22.3.0',
        'isort>=5.8.0,<6.0.0',
        'mypy>=0.910,<0.930',
    ],
    python_requires='>=3.8, <4',
    classifiers=[
        # Choose the appropriate classifiers from here: https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Replace if you have chosen a different license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='bikeshare, predictive modeling, data science',
    package_data={
        # Ensure the directory structure reflects where the file is located relative to the setup.py
        'bikeshare_model': ['datasets/bike-rental-dataset.csv'],
    },
    # Include additional configurations if needed
)

