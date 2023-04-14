
# =========================================
#       IMPORTS
# --------------------------------------

import os
import setuptools

# DISABLED/BUG: this line fails when `pip install attributedict` but works `pip install .`
# from attributedict import __version__


# =========================================
#       MAIN
# --------------------------------------

name = 'attributedict'
version = '0.3.0'
description = 'A dictionary object with attributes support - for Python.'
keywords = [
    'object',
    'dict',
    'dictionary',
    'collection',
    'attributes',
    'attribute',
    'attr',
    'properties',
    'property',
    'props',
    'openstruct',
    'struct',
    'hashmap',
]

packages = setuptools.find_packages(".")
requirements = [
    "rootpath @ git+https://github.com/reuben/python-rootpath.git@ced47237c25d39868d3ceb91af1f48b702469c99#egg=rootpath",
    "inspecta >= 0.1.3",
]
with open("README.md") as fin:
    readme = ''.join(fin.readlines())

config = {
    'name': name,
    'version': version,
    'description': (description),
    'keywords': keywords,
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'download_url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'project_urls': {
        'repository': 'https://github.com/grimen/python-{name}'.format(name = name),
        'bugs': 'https://github.com/grimen/python-{name}/issues'.format(name = name),
    },
    'license': 'MIT',

    'long_description': readme,
    'long_description_content_type': 'text/markdown',

    'classifiers': [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    'packages': packages,
    'package_dir': {
        name: name,
    },
    'package_data': {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        name: [
            '*.*',
        ],
    },
    'include_package_data': True,
    'zip_safe': True,

    'install_requires': requirements,
    'setup_requires': [
        'setuptools_git >= 1.2',
    ],
}

setuptools.setup(**config)
