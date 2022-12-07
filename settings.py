# -*- coding: utf-8 -*-
# filename          : settings.py
# description       : Different options for parts of the program
# author            : Ian Ault
# email             : aulti@csp.edu
# date              : 12-07-2022
# version           : v1.0
# usage             :
# notes             : This file should not be run directly
# license           : MIT
# py version        : 3.11.0
#==============================================================================
# Sets the IP/Domain Name and port to bind the API to, the API will only be
# accessable from whatever this is set to.
# The default value is "0.0.0.0" (for localhost) and 8080.
HOST = "0.0.0.0"
PORT = 8080

# Enables API serving via Flask instead of Waitress. Also disables downloading
# full media and skips verification checks.
# The default value is False.
DEBUG_MODE = False
