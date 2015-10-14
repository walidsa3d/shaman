from setuptools import find_packages
from setuptools import setup


setup(
    name='shaman',
    version='1.0',
    description="Movie info finder",
    long_description=open('README.md').read(),
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='https://github.com/walidsa3d/troov',
    license="MIT",
    keywords="movie film info imdb elcinema rottentomatoes themovidb",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": [""]},
    classifiers=[
        'Development Status :: 4  - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities'
    ]
)
