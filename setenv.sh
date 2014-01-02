# Source this script to set the PYTHONPATH for developing the gourl Django app
#
# NOTE: You must "source" this script by running one of the following commands:
#    . setenv.sh
#    source setenv.sh
# This script is intentionally *NOT* executable because running it will not
# set the environment variables of your shell.
#
# NOTE: This script *MUST* be run from the directory that contains it, as it
# uses the absolute path of the current directory when setting the PYTHONPATH.

export PYTHONPATH=$PWD/src:$PWD/site:$PWD/tests:$PYTHONPATH
echo PYTHONPATH=$PYTHONPATH
