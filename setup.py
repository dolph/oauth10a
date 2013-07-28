import setuptools


setuptools.setup(
    name='oauth10a',
    version='0.1.0',
    description='OAuth 1.0a for consumers and service providers.',
    author='Dolph Mathews',
    author_email='dolph.mathews@gmail.com',
    url='http://github.com/dolph/oauth10a',
    packages=['oauth10a'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'requests',
    ],
)
