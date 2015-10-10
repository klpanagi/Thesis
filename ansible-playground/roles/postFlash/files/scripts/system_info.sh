#!/bin/sh
#clear

# color list
colors ()
{
  RESET='\e[0m'
  BLACK='\e[1;30m'
  RED='\e[0;31m'
  GREEN='\e[0;32m'
  YELLOW='\e[0;33m'
  BLUE='\e[0;34m'
  PURPLE='\e[0;35m'
  CYAN='\e[0;36m'
  WHITE='\e[0;37m'

  BOIBLACK='\e[1;100m'
  BRED='\e[1;31m'
  BGREEN='\e[1;32m'
  BYELLOW='\e[1;33m'
  BBLUE='\e[1;34m'
  BPURPLE='\e[1;35m'
  BCYAN='\e[1;36m'
  BWHITE='\e[1;37m'
}; colors


if [ -e /etc/slackware-version ]
then
  distro=$(cat /etc/slackware-version)
elif [ 'cat /etc/issue.net | grep -q Debian' ]
then
  distro=$(cat /etc/issue.net | grep "Debian" | sed 's/%h//')
else
  distro=\ n/a
fi
name=$(uname -s)
version=$(uname -v)
hardware=$(uname -m)
release=$(uname -r)
mem=$(free -omt)
disk=$(df -lh 2> /dev/null)
hname=$(uname -n)
cpu=$(more /proc/cpuinfo | grep 'cpu MHz' | cut -d: -f2 | awk 'NR==3')
cpu_cores=$(cat /proc/cpuinfo | grep "siblings" | sort -u | cut -d: -f2)
cpumodel=$(cat /proc/cpuinfo | grep 'model name' | cut -d: -f2 | awk 'NR==1')
who=$(whoami)
lwho=$(logname)
uptime=$(uptime |sed 's/,.*$//')
total_mem=$(grep MemTotal /proc/meminfo | awk '{printf "%s MB", $2/1000}')
mem_use=$(free -m | awk 'NR==2{printf "%s/%s MB (%.2f)\n", $3,$2,$3*100/$2 }')
ifaces=$(ifconfig -a | sed 's/[ \t].*//;/^$/d')
#mem_dimm_slots=$(sudo lshw | grep DDR | cut -d':' -f2)
#----------------------------------------------------------------------



#Display information to user...
#------------------------------
echo -e "${YELLOW}-----------------<User Information>-----------------${RESET}"
echo -e "${BYELLOW}Currently logged in as${RESET}   **${BGREEN}$who${RESET}**"
echo -e "${BYELLOW}Originally logged in as${RESET}  **${BBLUE}$lwho${RESET}**"
echo -e "${BYELLOW}Hostname${RESET}                 **${BPURPLE}$hname${RESET}**"
echo -e ""
echo -e "${YELLOW}----------------<System Information>----------------${RESET}"
echo -e "  * ${BCYAN}OS Type${RESET}         --->  ${BRED}$name${RESET}"
#echo -e "Distro.                 : $distro"
echo -e "  * ${BCYAN}Kernel Version${RESET}  --->  ${BRED}$version${RESET}"
echo -e "  * ${BCYAN}Kernel Release${RESET}  --->  ${BRED}$release${RESET}"
echo -e "  * ${BCYAN}System Uptime${RESET}   --->  ${BRED}$uptime${RESET}"
echo -e "  * ${BCYAN}Architecture${RESET}    --->  ${BRED}$hardware${RESET}"
echo -e "  * ${BCYAN}CPU Cores${RESET}       --->  ${BRED}$cpu_cores${RESET}"
echo -e "  * ${BCYAN}CPU Model${RESET}       --->  ${BRED}$cpumodel${RESET}"
echo -e "  * ${BCYAN}CPU Speed${RESET}       --->  ${BRED}$cpu MHz${RESET}"
echo -e ""
echo -e "${YELLOW}----------------<Network Information>---------------${RESET}"
for i in ${ifaces}; do
  if [ "${i}" = "lo" ]; then
    continue
  fi
  ip=$(ip addr | grep inet | grep ${i} | awk -F" " '{print $2}'| sed -e 's/\/.*$//')
  echo -e "  *${BCYAN} ${i} ------> ${BGREEN}${ip}${RESET}"
done
echo -e ""
echo -e "${YELLOW}----------------<Memory Information>----------------${RESET}"
echo -e "  * ${BCYAN}Total Memory${RESET}  ---> ${BGREEN}$total_mem${RESET}"
echo -e "  * ${BCYAN}Memory usage${RESET}  ---> ${BGREEN}${mem_use}%${RESET}"
#echo -e "  * ${BCYAN}DIMM Slots${RESET}  ---> ${BGREEN}${mem_dimm_slots}%${RESET}"
#echo -e "  * ${BCYAN}System Memory in MB${RESET}"
#echo -e "$mem"
echo -e ""
echo -e "${YELLOW}-------------<Hard Disk(s) Information>-------------${RESET}"
echo -e "$disk"
echo
#echo
