from setuptools import setup, find_packages

setup(
    name="dj7n_allauth",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=4.2,<5.0",
        "django-allauth>=65.10.0",
        "requests>=2.32.4"
        "jwt>=1.4.0",
        "PyJWT>=2.10.1",
        "djangorestframework-simplejwt>=5.5.1"
    ],
    author="Bay Nguyen",
    author_email="baybknguyen@gmail.com",
    description="Dj7n Allauth for Django project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/baybk/dj7n_allauth.git",
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)