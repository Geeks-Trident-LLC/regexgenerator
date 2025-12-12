"""Packaging regexbuilder for distribution, installation, integration, and seamless deployment."""

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="regexbuilder",
    version="0.5.0a0",  # pre-beta versioning to signal alpha/beta status
    license="BSD-3-Clause",
    license_files=["LICENSE"],
    description="A versatile utility that generates regex patterns seamlessly"
                " from plain text or structured input, simplifying validation, "
                "filtering, and pattern‑matching workflows.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tuyen Mathew Duong",
    author_email="tuyen@geekstrident.com",
    maintainer="Tuyen Mathew Duong",
    maintainer_email="tuyen@geekstrident.com",
    install_requires=["pyyaml", "genericlib"],
    url="https://github.com/Geeks-Trident-LLC/regexbuilder",
    packages=find_packages(
        exclude=(
            "tests*", "testing*", "examples*",
            "build*", "dist*", "docs*", "venv*"
        )
    ),
    project_urls={
        "Documentation": "https://github.com/Geeks-Trident-LLC/regexbuilder/wiki",
        "Source": "https://github.com/Geeks-Trident-LLC/regexbuilder",
        "Tracker": "https://github.com/Geeks-Trident-LLC/regexbuilder/issues",
    },
    python_requires=">=3.9",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "regexbuilder = regexbuilder.main:execute",
            "regexbuilder-gui = regexbuilder.application:execute",
            "regexbuilder-app = regexbuilder.application:execute",
            "regex-builder-gui = regexbuilder.application:execute",
            "regex-builder-app = regexbuilder.application:execute",
        ]
    },
    classifiers=[
        # development status
        "Development Status :: 3 - Alpha",
        # natural language
        "Natural Language :: English",
        # intended audience
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        # operating system
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        # programming language
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        # topic
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Scientific/Engineering",
        "Topic :: Text Processing",
    ],
    keywords="regex, regex builder, regexbuilder, text parsing, automation, regular express",
)