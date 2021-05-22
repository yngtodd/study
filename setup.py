from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()


setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest>=3', ]
requirements = ['argh',]


COMMANDS = [
    'greet = study.cli:greet',
]


setup(
    author="Todd Young",
    author_email="yngtdd@mgail.com",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An art study approach to machine learning.",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='study',
    name='study',
    packages=find_packages(include=['study', 'study.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yngtodd/study',
    version='0.1.0',
    zip_safe=False,
)
