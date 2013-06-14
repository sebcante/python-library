from distutils.core import setup


setup(
    name="urbanairship",
    version="0.6",
    author="Adam Lowry",
    author_email="adam@urbanairship.com",
    url="http://urbanairship.com/",
    description="Python package for using the Urban Airship API",
    long_description=open('README.rst').read(),
    packages=["urbanairship", "urbanairship.push"],
    license='BSD License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'
    ],
)
