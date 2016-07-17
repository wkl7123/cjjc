if [ ! -d "$HOME/.cjjc" ]; then
    mkdir $HOME/.cjjc/
    cp cj.py $HOME/.cjjc/
    cp jc.py $HOME/.cjjc/
    echo -e "\nalias jc='python2 $HOME/.cjjc/jc.py'">>$HOME/.bashrc
    echo -e "\nalias cj='python2 $HOME/.cjjc/cj.py'">>$HOME/.bashrc
else
    rm -r $HOME/.cjjc/
    mkdir $HOME/.cjjc/
    cp cj.py $HOME/.cjjc/
    cp jc.py $HOME/.cjjc/
    echo -e "\nalias jc='python2 $HOME/.cjjc/jc.py'">>$HOME/.bashrc
    echo -e "\nalias cj='python2 $HOME/.cjjc/cj.py'">>$HOME/.bashrc
fi


