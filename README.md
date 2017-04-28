# (Item2vec) Recommendation-based-on-sequence-
People do not always buy things randomly but they buy them in some order. For example, you first buy the motorbike and then the helmet. Or you first see the Harry Potter 1 and then the Harry Potter 2. 
This is an advanced recommendation algorithm that proposes items to the user based on the sequences  of items they buy or interact with previously. 

Input is a sequences of items that users have done in the past. For example, entries of the form: < user, item1, item2, …, itemK>. 

# Requirements 

Item2vec requires gensim an open-source vector space modeling and topic modeling toolkit, implemented in the Python
programming language. I

# Quick install

Run in your terminal:

-- easy_install -U gensim

or, alternatively:

--pip install --upgrade gensim

In case that fails, make sure you’re installing into a writeable location (or use sudo), or read on.

# Dependencies

Gensim is known to run on Linux, Windows and Mac OS X and should run on any other platform that supports Python 2.6+ and NumPy. Gensim depends on the following software:

Python >= 2.6. Tested with versions 2.6, 2.7, 3.3, 3.4 and 3.5. Support for Python 2.5 was discontinued starting gensim 0.10.0; if you must use Python 2.5, install gensim 0.9.1.

NumPy >= 1.3. Tested with version 1.9.0, 1.7.1, 1.7.0, 1.6.2, 1.6.1rc2, 1.5.0rc1, 1.4.0, 1.3.0, 1.3.0rc2.

SciPy >= 0.7. Tested with version 0.14.0, 0.12.0, 0.11.0, 0.10.1, 0.9.0, 0.8.0, 0.8.0b1, 0.7.1, 0.7.0.

Windows users are well advised to try the Enthought distribution, which conveniently includes Python & NumPy & SciPy in a single bundle, and is free for academic use.

# Installation

Check what version of Python you have with:

python --version

You can download Python from http://python.org/download.

Note
Gensim requires Python 2.6 / 3.3 or greater, and will not run under earlier versions.

### Install SciPy & NumPy¶
These are quite popular Python packages, so chances are there are pre-built binary distributions available for your platform. You can try installing from source using easy_install:

easy_install numpy
easy_install scipy
If that doesn’t work or if you’d rather install using a binary package, consult http://www.scipy.org/Download.

# Install gensim

You can now install (or upgrade) gensim with:

easy_install --upgrade gensim


If you also want to run the algorithms over a cluster of computers, in Distributed Computing, you should install with:

easy_install gensim[distributed]



## Project report can be found here 
https://www.researchgate.net/publication/316527587_Recommendation_based_on_sequence_Item2vec

