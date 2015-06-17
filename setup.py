from setuptools import setup

setup(
    name="mastermind",
    version="2.25",
    author="Andrey Vasilenkov",
    author_email="indigo@yandex-team.ru",
    url="https://github.com/yandex/mastermind",
    description="Common components and a client library for Mastermind",
    long_description="",
    license="LGPLv3+",
    packages=[
        "mastermind",
    ],
    package_dir={'mastermind': 'src/python-mastermind/src/mastermind'},
    install_requires=["cocaine_framework_python", "tornado >= 3.0"],
)