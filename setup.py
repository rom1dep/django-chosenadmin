from setuptools import setup
from chosenadmin import __version__


url = "https://github.com/bradmontgomery/django-chosenadmin/archive/v{0}.tar.gz".format(__version__)

setup(
    name="django-chosenadmin",
    version=__version__,
    author="Brad Montgomery",
    author_email="brad@bradmontgomery.net",
    description=("Adds Chosen.js to the Django Admin app"),
    install_requires=[],
    license="MIT",
    keywords="django chosen admin",
    url=url,
    packages=[
        "chosenadmin",
    ],
    include_package_data=True,
    package_data={'': ['**/*.*']},
    long_description="Adds the Chosen.js plugin to Select and Multi-select elements in Django's admin.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
        "Topic :: Utilities",
    ],
)
