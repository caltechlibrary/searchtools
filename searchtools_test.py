#!/usr/bin/env Python3

import os
import sys

# package to test
import searchtools 


def test_logger():
    ok = True
    log = searchtools.Logger(os.getpid())
    msg = 'This is a log message'
    if __debug__: 
        print(f'Expect "{msg}" with a timestamp and pid prefix')
        log.print(msg)
    s = log.sprint(msg)
    if not (msg in s):
        print(f'Expected "{msg}" in s: "{s}"')
        ok = False
    return ok

def test_empty_config():
    ok = True
    cfg = searchtools.Configuration()
    # NOTE: cfg has been created but not loaded yet.
    organization = cfg.get('organization', False)
    if organization != False:
        print(f'Expected False for organization, got "{organization}"')
        ok = False
    return ok

def test_config():
    ok = True
    f_name = os.path.join("tests", "test_config.json")
    cfg = searchtools.Configuration()
    if not cfg.load_config(f_name):
        print(f'Failed to load {f_name}')
        ok = False
    keys = [ "elastic_documents", "site_title", "organization" ]
    if not cfg.required(keys):
        print(f'Expected "{", ".join(keys)}", required = False')
        print(cfg.toJSON())
        ok = False
    key_list = cfg.keys()
    for key in key_list:
        if not key in keys:
            print(f'Expected key {key} in required keys {keys}')
            ok = False
    for key in keys:
        if not key in key_list:
            print(f'Expected key {key} in key list {keys}')
            ok = False
    print(f'Expect warning about missing "beanstalk" on {f_name}')
    keys = [ "beanstalk" ]
    expected = False
    value = cfg.required(keys)
    if expected != value:
        print(f'Expected {expected}, got {value} for keys "{keys}"')
        print(cfg.toJSON())
        ok = False
    key = "elastic_documents"
    expected = True
    value = cfg.get(key, False)
    if not (value == 'elastic-documents.json'):
        print(f'Expected "elastic-documents.json", got "{value}" for {key}')
        #print(cfg.toJSON())
        ok = False
    key = 'beanstalk'
    value = cfg.get(key, "Hello World")
    if value != "Hello World":
        print(f'Expected (default) "Hello World", got "{value}" for {key}')
        print(cfg.toJSON())
        ok = False
    return ok

if __name__ == '__main__':
    if not test_logger():
        print('test_logger() failed.')
        sys.exit(1)
    if not test_empty_config():
        print('test_empty_config() failed.')
        sys.exit(1)
    if not test_config():
        print('test_config() failed.')
        sys.exit(1)
    print('OK')
    sys.exit(0)
