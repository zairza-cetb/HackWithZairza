from setuptools import setup

setup(
    name="todo-cli",
    version="1.0.0",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "todo=todo:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.6",
    author="Your Name",
    description="Interactive command-line Todo CLI with add/list/edit/filter tasks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
