# Comparing Version Strings

### Code
The code is found in `./versionString/version_compare.py.` and the tests in `test_compare.py`.

I implemented my comparison to handle many different cases and different versions. 
Here's a quick list of valid version strings that my code can handle:
* 1.1
* 1.1.1
* 1.1a5
* 1.1.dev50
* 1.1.post50
* 1.1rc5.dev40
* 1.1.3.post45.dev10

However, there are some cases that are not covered: 
* 1.0+abc.5
* 1.0+5
* 2020.1

### Library
For the library part, I added the `__init__.py` in the versionString folder so python can treat it as a package. Then, I create setup.py and setup the library by running `python3 setup.py sdist` on the command line which creates the dist directory and `version_compare.egg-info`.

To download the library, you simply run `pip3 install ./dist/version_compare-0.0.1.tar.gz` in this directory in the command line. 

Then, you can test that it was properly downloaded by running `python3` and then writing `>>> from versionString import version_compare` on the shell. You can then use the function `version_compare.compare(version1, verson2)`

Of course, to uninstall, simply type `pip3 uninstall version-compare`