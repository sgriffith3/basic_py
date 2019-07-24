# Helpful Tips

**A continuosly growing list of helpful tips I have come across while teaching hundreds of students.**

### Topics Include:

* _Python(3)_

* _Ansible_

* _Ubuntu_

* _Vim_

* _Tmux_

* _Kubernetes_


### Vim

0. In order to auto-generate a shebang line in a new Vim document, you need to associate a file type in your `/etc/vim/vimrc` file. The following code, added to the vimrc file, will allow vim to immediately place the Python3 shebang line at the top of the file.

    `$` `sudo vim /etc/vim/vimrc`
    
    Then add the following before the end of the file:
    
    ```
    autocmd BufNewFile *.py execute 'silent! 1s:.*:#!/usr/bin/env python3'

    if has("autocmd")
      filetype plugin indent on
    endif
    ```
    
    If you would like to use this for other types of scripts, you could replace the `BufNewFile *.py` with, let's say, `BufNewFile *.sh`, then edit the shebang line to match your needs.

