# pylint: disable = C0111
from setuptools import find_packages, setup

with open("../README.md", "r", encoding="utf-8") as f:
    # Remove GitHub dark mode images
    DESCRIPTION = "".join([line for line in f if "gh-dark-mode-only" not in line])

setup(
    name="ncoder",
    version="0.1.0",
    author="NeuML",
    description="Jupyter notebook plugin to generate code with AI",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/neuml/ncoder",
    project_urls={
        "Documentation": "https://github.com/neuml/ncoder",
        "Issue Tracker": "https://github.com/neuml/ncoder/issues",
        "Source Code": "https://github.com/neuml/ncoder",
    },
    license="Apache 2.0: http://www.apache.org/licenses/LICENSE-2.0",
    packages=find_packages(where="src/python"),
    package_dir={"": "src/python"},
    keywords="ai ai-coding",
    python_requires=">=3.10",
    install_requires=["ipython>=8.35.0", "openai>=1.100.2"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
    ],
)
