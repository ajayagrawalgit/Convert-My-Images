#!/bin/bash
clear;
echo -e "


:'######::'#######:'##::: ##'##::::'##'########'########:'########::::::::'##::::'##'##:::'##::::::::'####'##::::'##:::'###::::'######::'########:'######::
'##... ##'##.... ##:###:: ##:##:::: ##:##.....::##.... ##... ##..::::::::::###::'###. ##:'##:::::::::. ##::###::'###::'## ##::'##... ##::##.....:'##... ##:
 ##:::..::##:::: ##:####: ##:##:::: ##:##:::::::##:::: ##::: ##::::::::::::####'####:. ####::::::::::: ##::####'####:'##:. ##::##:::..:::##:::::::##:::..::
 ##:::::::##:::: ##:## ## ##:##:::: ##:######:::########:::: ##:::'#######:## ### ##::. ##:::'#######: ##::## ### ##'##:::. ##:##::'####:######::. ######::
 ##:::::::##:::: ##:##. ####. ##:: ##::##...::::##.. ##::::: ##:::........:##. #: ##::: ##:::........: ##::##. #: ##:#########:##::: ##::##...::::..... ##:
 ##::: ##:##:::: ##:##:. ###:. ## ##:::##:::::::##::. ##:::: ##::::::::::::##:.:: ##::: ##:::::::::::: ##::##:.:: ##:##.... ##:##::: ##::##::::::'##::: ##:
. ######:. #######::##::. ##::. ###::::########:##:::. ##::: ##::::::::::::##:::: ##::: ##:::::::::::'####:##:::: ##:##:::: ##. ######:::########. ######::
:......:::.......::..::::..::::...::::........:..:::::..::::..::::::::::::..:::::..::::..::::::::::::....:..:::::..:..:::::..::......:::........::......:::

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
A N     O P E N - S O U R C E     U T I L I T Y     T O     C O N V E R T     I M A G E S     I N     B U L K
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 How to use ?
 Very Simple... Just follow this syntax and you'll be set 😉
 convertmyimages <source_path> <destination_path> <initial_format> <final_format>

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Developed by Ajay Agrawal | Github: https://github.com/ajayagrawalgit
Support me if you like my work : https://www.buymeacoffee.com/ajayagrawal

Cheers 🥂 

_______________________________________________________________________________


"


PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>&1)
if [ -n "$PYTHON_VERSION" ] && [ "$(echo "$PYTHON_VERSION" | awk -F. '{ printf("%03d%03d%03d\n", $1,$2,$3); }')" -lt "$(echo '3.11.2' | awk -F. '{ printf("%03d%03d%03d\n", $1,$2,$3); }')" ]; then
  echo "Upgrading to Python 3.11.2"
  if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install python@3.11
  elif [[ -f /etc/redhat-release ]]; then
    # RHEL/CentOS
    sudo yum update -y
    sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    sudo yum install -y python3.11
  else
    # Debian/Ubuntu
    sudo apt-get update
    sudo apt-get install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt-get update
    sudo apt-get install -y python3.11
  fi
else
  echo "Python version is already up to date"
fi


# Install required packages
echo "Installing required packages"
pip3 install -r requirements.txt
if [[ $? -ne 0 ]]; then
  echo "Failed to install required packages"
  exit 1
fi




cur_dir=$(pwd)

# set the file/directory path
LIB_PATH="/usr/local/lib/convert-my-images" # Complete Code
BIN_PATH="/usr/local/bin/convertmyimages"   # Soft Link to he file

if [[ -e "$LIB_PATH" ]]; then
    echo -e "Library convert-my-images already exists on your machine. Hence, Removing it first before installing.."
    sudo rm -rf $LIB_PATH
    echo -e "convert-my-images library and its contents removed 👍"
else
  echo "Great 👍 No Libraries matching convertmyimages present on your machine\n"
fi

sleep 5
echo -e "\n\n- - - - - - - - - - - - - - - - - - - -\n\n"

if [ -L $BIN_PATH ]; then
    echo -e "Cleanup Required for removing all the older contents of convert-my-images..."
    echo -e "Don't worry ! Everything will be done automatically 😊"
    sudo rm -f $BIN_PATH
    echo -e "All the Older files for convert-my-images removed successfully from your machine 👍"
else
  echo "No older versions/files detected on your machine for convert-my-images installed 👍"
fi
sleep 5;

echo -e "\n\n- - - - - - - - - - - - - - - - - - - -\n\n"

echo -e "$(date): Starting the Installation now ..."

#!/bin/bash

function install() {
  mkdir $LIB_PATH
  if [ $? -ne 0 ]; then
    echo "/usr/local/ not accessible !"
    return 1
  fi

  echo "Copying necessary files now ..."
  cp -r $cur_dir $LIB_PATH
  if [ $? -ne 0 ]; then

    echo "Installation Failed"
    return 1
  fi

  echo "Creating Soft Link ..."
  ln -s $LIB_PATH/src/convertmyimages.sh $BIN_PATH
  if [ $? -ne 0 ]; then
    echo "Installation Failed"
    return 1
  fi

  echo "Installation Completed successfully"
}

install
if [ $? -eq 0 ]; then
  echo -e "$(date): Installation Completed Successfully"
else
  echo "$(date): Installation Failed !"
fi




echo -e "Now try running just a simple command -> convertmyimages\n\n\nThanks for Installing 😁\n\n\n"
