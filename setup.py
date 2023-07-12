"""Packaging regexpro."""

from setuptools import setup, find_packages


setup(
    name='regexpro',
    version='0.3.12',
    license='Geeks Trident License',
    license_files=['LICENSE'],
    description='The application to generate regex pattern.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tuyen Mathew Duong',
    author_email='tuyen@geekstrident.com',
    maintainer='Tuyen Mathew Duong',
    maintainer_email='tuyen@geekstrident.com',
    install_requires=['pyyaml', ],
    url='https://github.com/Geeks-Trident-LLC/regexpro',
    packages=find_packages(
        exclude=(
            'tests*', 'testing*', 'examples*',
            'build*', 'dist*', 'docs*', 'venv*'
        )
    ),
    include_package_data=True,
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'regexpro = regexpro.main:execute',
            'regex-pro = regexpro.application:execute',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
