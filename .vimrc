colorscheme desert
syntax enable       " enable syntax
filetype indent on
set tabstop=8       " number of visual spaces per tab
set softtabstop=4   " number of spaces when editing
set shiftwidth=4
set expandtab       " tabs are spaces
set number	    " line numbers
set showcmd
set incsearch       " search as you type
set hlsearch        " highlight matches

nnoremap <buff> <2> :exec "!python" shellescape(0%, 1)<cr>
nnoremap <buff> <3> :exec "!python3" shellescape(0%, 1)<cr>
