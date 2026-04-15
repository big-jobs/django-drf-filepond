from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="django-drf-filepond",
    version="0.5.2.2",
    description="Filepond server app for Django REST Framework",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Jeremy Cohen",
    author_email="jeremy.cohen@imperial.ac.uk",
    url="https://github.com/ImperialCollegeLondon/django-drf-filepond",
    download_url=(
        "https://github.com/ImperialCollegeLondon/django-drf-filepond.git"),
    license="BSD 3-Clause",
    packages=[
        "django_drf_filepond",
        "django_drf_filepond.migrations",
    ],
    include_package_data=True,
    install_requires=[
        "Django>=4.2.26",
        "djangorestframework>=3.15.2",
        "shortuuid>=0.5.0",
        "requests>=2.20.1",
        "django-storages>=1.9.1",
        "sorl-thumbnail>=12.10.0",
    ],
    tests_require=[
        "nose",
        "coverage",
        "httpretty>=1.0.3",
        "mock>=3.0.5",
        "paramiko"
    ],
    zip_safe=False,
    test_suite="tests.runner.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
