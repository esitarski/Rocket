# -*- coding: utf-8 -*-

# This file is part of the Rocket Web Server
# Copyright (c) 2009 Timothy Farrell

# Import System Modules
import sys
import errno
import platform

# Define Constants
VERSION = '0.1'
SERVER_NAME = 'Rocket %s' % VERSION
HTTP_SERVER_NAME = '%s Python/%s' % (SERVER_NAME, sys.version.split(' ')[0])
BUF_SIZE = 16384
IS_JYTHON = platform.system() == 'Java' # Handle special cases for Jython
IGNORE_ERRORS_ON_CLOSE = set([errno.ECONNABORTED, errno.ECONNRESET])
DEFAULT_QUEUE_SIZE = 5
DEFAULT_MIN_THREADS = 10
DEFAULT_MAX_THREADS = 128
DEFAULTS = dict(QUEUE_SIZE = DEFAULT_QUEUE_SIZE,
                MIN_THREADS = DEFAULT_MIN_THREADS,
                MAX_THREADS = DEFAULT_MAX_THREADS)

PY3K = sys.version_info[0] > 2

def close_socket(sock):
    if hasattr(sock, '_sock'):
        try:
            sock._sock.close()
        except socket.error:
            a, b, c = sys.exc_info()
            if b.errno != errno.EBADF:
                raise b
            else:
                pass
    sock.close()

if PY3K:
    def b(n):
        """ Convert string/unicode/bytes literals into bytes.  This allows for
        the same code to run on Python 2.x and 3.x. """
        if isinstance(n, str):
            return n.encode()
        else:
            return n

    def u(n, encoding="us-ascii"):
        """ Convert bytes into string/unicode.  This allows for the
        same code to run on Python 2.x and 3.x. """
        if isinstance(n, bytes):
            return n.decode(encoding)
        else:
            return n

else:
    def b(n):
        """ Convert string/unicode/bytes literals into bytes.  This allows for
        the same code to run on Python 2.x and 3.x. """
        if isinstance(n, unicode):
            return n.encode()
        else:
            return n

    def u(n, encoding="us-ascii"):
        """ Convert bytes into string/unicode.  This allows for the
        same code to run on Python 2.x and 3.x. """
        if isinstance(n, str):
            return n.decode(encoding)
        else:
            return n

__all__ = ['VERSION', 'SERVER_NAME', 'HTTP_SERVER_NAME', 'BUF_SIZE',
           'IS_JYTHON', 'IGNORE_ERRORS_ON_CLOSE', 'DEFAULTS', 'PY3K', 'b', 'u']
