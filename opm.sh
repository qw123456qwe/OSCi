#!/usr/bin/env bash

CMD=$1
PKG=$2

INDEX="https://raw.githubusercontent.com/qw123456qwe/opm-index/main/packages.json"

if [ "$CMD" = "install" ]; then

    URL=$(curl -s $INDEX | grep "\"$PKG\"" -A1 | grep http | tr -d '", ')

    if [ -z "$URL" ]; then
        echo "Package topilmadi: $PKG"
        exit 1
    fi

    echo "Installing $PKG from $URL"

    git clone $URL
    cd $(basename $URL .git)

    if [ -f "install.sh" ]; then
        bash install.sh
    else
        echo "install.sh topilmadi"
    fi

fi
