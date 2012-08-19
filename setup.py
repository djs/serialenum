"""
serialenum
----------

A cross-platform serial port enumerator utility function. Use with pyserial to
automatically detect available serial ports on any system.

For more information, see the `github page <https://github.com/djs/serialenum>`_.
"""


from setuptools import setup, find_packages

setup(
    name = "serialenum",
    version = "0.1",
    py_modules = ['serialenum'],
    author = "Dan Savilonis",
    author_email = "djs@n-cube.org",
    url = 'https://github.com/djs/serialenum',
    description = "Cross-platform serial port enumeration",
    license = "BSD",
    keywords = "serial serial-port",
    long_description = __doc__,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
