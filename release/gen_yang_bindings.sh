#!/bin/bash

PYBINDPLUGIN=`python -c 'import pyangbind; import os; print("{}/plugin".format(os.path.dirname(pyangbind.__file__)))'`
YANG_SEARCH_PATH=models:models/types:models/system
YANG_FILES=$(find models -name "*.yang")
CLASS_DIRS=$(find models -type d | tr '-' '_' | sed 's/models/classes/')

for dir in $CLASS_DIRS
do
    mkdir -vp $dir
    touch $dir/__init__.py 
done

exit

for yang_file in $YANG_FILES
do
    python_file=$(echo $yang_file | sed 's/models/classes/; s/yang/py/; s/-/_/g;')
    echo "generating code from ${yang_file} to ${python_file}"
    pyang -V --plugindir $PYBINDPLUGIN -f pybind -p $YANG_SEARCH_PATH -o $python_file $yang_file
done
