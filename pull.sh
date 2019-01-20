#!/usr/bin/env bash

python scripts/build.py
sfdx force:source:retrieve -x manifest/package.xml
