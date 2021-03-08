#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run jovyan123-playground Bot.
"""

# Local imports
from jovyan123_playground_bot.webapp import main
from jupyterlab_bot.config import PORT


if __name__ == "__main__":
    print('\nRunning jovyan123-playground Bot on: http://localhost:5000\n')
    print('Press Ctrl+C to exit\n\n')
    main()
