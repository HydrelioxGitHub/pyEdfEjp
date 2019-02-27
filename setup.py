from distutils.core import setup

setup(
    name='pyEdfEjp',
    packages=['pyEdjEjp'],  # this must be the same as the name above
    install_requires=['urllib.request'],
    version='0.1-beta',
    description='a simple python3 library for the E.D.F. EJP Pricing',
    author='Hydreliox',
    author_email='hydreliox@gmail.com',
    url='https://github.com/HydrelioxGitHub/pyEdfEjp',  # use the URL to the github repo
    download_url='https://github.com/HydrelioxGitHub/pyEdfEjp/tarball/0.1-beta',
    keywords=['EDF', 'EJP', 'Energy', 'API'],  # arbitrary keywords
    classifiers=[],
)
