export PATH="$PATH:/Users/Shmuli/Library/Python/3.9/bin"
export PATH="$PATH:/Users/Shmuli/scripts"
export PATH="$PATH:/Users/Shmuli/downloads/go/bin"
export PATH="$HOME/.local/bin:$PATH"


# source /Users/Shmuli/coding-projects/wasm/emsdk/emsdk_env.sh


alias fp="git add * && git commit -m 'empty commit message' && git push"
alias code="open -a 'visual studio code' $1"
alias .="code ."
alias uv="uvicorn main:app --reload"
alias p="python3 main.py"
alias run='function run_cpp { g++ -std=c++20 "$1.cpp" -o "$1" && ./"$1"; }; run_cpp'
alias cz="code ~/.zshrc"
alias sz="source ~/.zshrc"
alias m="run main"
alias clean="mv *.png images/; mv *.jpg images/"
alias scatter="mv images/*.png .; mv images/*.jpg ."
alias ir="python3 -m pip install -r requirements.txt"
alias pdp="./pythonDynamicPush.sh"
alias sz="source ~/.zshrc; echo 'sourced zshrc'"
alias gl="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
alias repo="cd ~/repositories; ls"
alias co="cd ~/coding-projects; ls"
alias p="python3 ."
alias gnb="git checkout -b"
alias gb="git branch"
alias gm="git switch main"
alias wasmCompile="emcc ../main.cpp -o main.js -s EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]'"
# alias g-s="git init; git add .; git commit -m 'initial commit'; git remote add origin https://github.com/Shmuli/coding-projects.git; git push -u origin main"

alias o=" open main.html"
PATH=~/.console-ninja/.bin:$PATH
alias c="clear"