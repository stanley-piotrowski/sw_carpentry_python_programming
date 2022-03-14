#!/bin/bash

# Download zipped inflammation data directory and extract contents
URL="https://swcarpentry.github.io/python-novice-inflammation/data/python-novice-inflammation-data.zip"
wget --verbose ${URL}

# Extract files
ZIP_ARCHIVE=`basename ${URL}`
unzip ${ZIP_ARCHIVE}

# Remove old zip archive
rm -rf ${ZIP_ARCHIVE}
