from setuptools import setup

setup(
    name='todo_kafka',
    version='0.1.0',
    py_modules=['app'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'todo = app:cli',
        ],
    },
)
