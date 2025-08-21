PROMPT='%F{cyan}%n%F{white}@%F{blue}%~ %F{cyan}> %F{white}'

http_proxy=http://192.168.0.230:10808
socks_proxy=http://192.168.0.230:10808

alias proxyon="export http_proxy=$http_proxy; export https_proxy=$http_proxy; export all_proxy=$socks_proxy; echo 'proxy on...'"

alias proxyoff="unset http_proxy; unset https_proxy; unset all_proxy; echo 'proxy off...'"

alias hugon="hugo server --bind 192.168.0.22 --baseURL 192.168.0.22; echo 'server started...'"

alias gptt="export GPG_TTY=$(tty)"

alias pyin="python -m venv .venv"

alias pyon="source .venv/bin/activate"

alias pyoff="deactivate"

alias ls="lsd -al"

alias pyfmt="python ~/app/pyfmt.py"

export GPG_TTY=$(tty)
