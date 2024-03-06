#!/bin/bash

. .venv/bin/activate

#LOG_FILE="build.log"
#DATA_FILE="data.json"
#SOURCE_FILES=$(find . -name index.mustache)
#
#for SOURCE_FILE in $SOURCE_FILES; do
#  OUTPUT_FILE="$(dirname ${SOURCE_FILE})/index.html"
#  echo "convert ${SOURCE_FILE} to ${OUTPUT_FILE}"
#  chevron -d "${DATA_FILE}" -d "$(dirname $SOURCE_FILE})/data.json" -p _partials "${SOURCE_FILE}" > "${OUTPUT_FILE}"
#  echo "${OUTPUT_FILE}" >> "${LOG_FILE}"
#done

python3 build.py

python3 -m http.server
