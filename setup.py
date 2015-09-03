from distutils.core import setup


setup(
    name='cort',
    version='0.2.2',
    packages=['cort',
              'cort.analysis',
              'cort.core',
              'cort.test',
              'cort.coreference',
              'cort.test.multigraph',
              'cort.test.analysis',
              'cort.test.core',
              'cort.coreference.multigraph',
              'cort.coreference.approaches',
              'cort.util',
              'cort.preprocessing',
              'stanford_corenlp_pywrapper'],

    url='http://github.com/smartschat/cort',
    license='MIT',
    author='Sebastian Martschat, Thierry Goeckel, Patrick Claus',
    author_email='sebastian.martschat@gmail.com',
    description='A coreference resolution research toolkit.',
    keywords = ['NLP', 'CL', 'natural language processing',
                'computational linguistics', 'coreference resolution',
                'text analytics'],
    classifiers = [
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing',
        ],
    install_requires=['nltk >= 3.0.1', 'numpy', 'matplotlib', 'mmh3', 'cython',
                      'future', 'jpype1', 'beautifulsoup4',
                      'pystanforddependencies >= 0.2.0'],
    package_data={
        'cort': ['analysis/visualization/style.css',
                 'analysis/visualization/lib/*',
                 'resources/*',
                 'config_files/*',
                 'coreference/perceptrons.pyx',
                 "reference-coreference-scorers/v8.01/*.*",
                 "reference-coreference-scorers/v8.01/lib/*.pm",
                 "reference-coreference-scorers/v8.01/lib/Algorithm/*",
                 "reference-coreference-scorers/v8.01/lib/Data/*",
                 "reference-coreference-scorers/v8.01/lib/Math/*"],
        'stanford_corenlp_pywrapper': ['rcorenlp.r',
                                       'lib/*',
                                       'javasrc/corenlp/*',
                                       'javasrc/util/misc/*',
                                       'javasrc/util/*.java'],
    },
    scripts=['bin/cort-train', 'bin/cort-predict-conll',
             'bin/cort-predict-raw', 'bin/cort-visualize',
             'bin/run-multigraph']
)
