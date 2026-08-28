#!/bin/bash

set -e

scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

pushd ${scriptdir}/..

for r in pkg docs tests dev; do
    echo ""
    echo "----------------------------"
    echo -e "Requirement: \033[1m${r}\033[0m"
    pip-compile -r -U requirements/${r}.in
done

popd
