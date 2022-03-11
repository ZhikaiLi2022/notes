# Simple steps to build your strongest terminal
> Most important words---Instead of the mouse, you need to fly.
***
## Preface

## <h2 id="0"> content </h2>
#### 1.[Regolith](#1)
* ###### 1.1 introduction of regolith
* ###### 1.2 regolith install
* ###### 1.3 Configuration of regolith 
#### 2.[Ranger](#2)
* ###### 2.1 introduction of ranger
* ###### 2.2 ranger install
* ###### 2.3 configuration of ranger
* ###### 2.4 configuration files of ranger
#### 3.[Neovim](#3)
* ###### 3.1 introduction of regolith
* ###### 3.2 neovim install
* ###### 3.3 Configuration of neovim
* ###### 3.4 configuration files of neovim
* ###### 3.5 usful plug-in
#### 4.[GitHub](#4)
* ###### 4.1 introduction of GitHub
* ###### 4.2 neovim install
* ###### 4.3 Configuration of GitHub
* ###### 4.4 configuration files of neovim

---
##1
## <h2 id="1"> 1.Regolith[^](#0) </h2>
#### **1.1 Introduction:** 
&emsp;**[Regolith](https://regolith-linux.org/)** is a modern desktop environment designed to let you work faster by reducing unnecessary clutter and cerenony.Built on top of Ubuntu,GNOME,and i3,Regolith stands on a well-supported and consistent foundation.
 
 ![desktop of regolith](https://regolith-linux.org/images/screenshot-terminals.png) 
---

#### **1.2 Regolith install:** 
Regolith can be installed in an existing Ubuntu 18.04 up system by adding a Regolith PPA and installing one of [the regolith-desktop packages](https://regolith-linux.org/docs/getting-started/install/#desktop-packages).Advantages to Regolith via PPA:
 * More compatibility with standard Ubuntu
 * Easy interop with other installed desktop environments
 * Keep existing system installation
 * Easy to remove and return to other desktop environments
 TO install the standard variant of Regolith Desktop from the release PPA:
 ```sh
 $ sudo add-apt-repository ppa:regolith-linux/release
 $ sudo apt install regolith-desktop-standard
 ```
 Learn more about [adding PPAs here](https://help.ubuntu.com/community/Repositories/CommandLine#Adding_Launchpad_PPA_Repositories),and more about[PPAs that Regolith provides here](https://regolith-linux.org/docs/getting-started/install/#ppa-sources) .

#### **1.3 Configuration of Regolith:** 
* **Super + c** helping you to change wallpaper or other setting,such as wifi,Bluetooth and power as like.

 ![Background](https://regolith-linux.org/images/regolith-screenshot-settings-wallpaper.png)
---

* **Super + Enter** -------------------------------------Launch Terminal
* **Super + Shift + Enter** ---------------------------Launch Browser
* **Super + Space** ------------------------------------Launch Application
* **Super + Ctrl + Space** ----------------------------Choose Window
---
* **Super + number** ---------------------------------Go to Workspace number
* **Super + Tab** ---------------------------------------Next Workspace
* **Super + Shift + Tab** -----------------------------Last Workspace
---
* **Super + Backspace** -----------------------------Toggle Layout Mode
---
* **Super + r** -------------------------------------------Resize Window Mode
* **Escape** ----------------------------------------------Exit Resice Window Mode
* **Super + f** -------------------------------------------Focused Window Fullscreen Toggle
* **Super + Shift + f** ---------------------------------Floating Window MOde Toggle
* **Super + Shift + q** --------------------------------Kill Active Window
---
* **Super + Shift + number** -----------------------Move Window to WS number
---
* **Super + direction key** --------------------------Change Window Focus
* **Super + Shift + direction key** ----------------Move Window
---
* **Super + [+/-]** --------------------------------------Resize Window Gaps
---
* **Super + c** -------------------------------------------Control Center
---
* **Super + Escape** -----------------------------------Lock Screen
* **Super + Shift + s** ---------------------------------Sleep
* **Super + Shift + e** ---------------------------------Logout
---
* **Super + Shift + ?** ---------------------------------Toggle helping Window
---
## <h2 id="2"> 2.Ranger[^](#0) </h2>
#### **2.1 Introduction of ranger:** 
&emsp;**[ranger](http://ranger.github.io/)** is a console file manager with VI key bindings. It provides a minimalistic and nice curses interface with a view on the directory hierarchy. It ships with [rifle](https://github.com/ranger/ranger/blob/master/ranger/ext/rifle.py),a file launcher that is good at automatically finding out which program to use for what file type.

  ![ranger](http://ranger.github.io/screenshots/screenshot0.png) 
---
**Design Goals**
* An easily maintainable file manager in a high level language
* A quick way to switch directories and browse the file system
* Keep it small but useful, do one thing and do it well
* Console-based, with smooth integration into the unix shell
---
**Features**
* UTF-8 Support (if your Python copy supports it)
* Multi-column display
* Preview of the selected file/directory
* Common file operations (create/chmod/copy/delete/...)
* Renaming multiple files at once
* VIM-like console and hotkeys
* Automatically determine file types and run them with correct programs
* Change the directory of your shell after exiting ranger
* Tabs, bookmarks, mouse support...
---

#### **2.2 To Install ranger in Ununtu:**
Use the package manager of your operating system to install ranger. You can also install ranger through key
```sh
$ sudo apt-get install ranger
```
#### **2.3 Configuration of ranger:**
you can finding useful keybindings in its [GitHub](https://github.com/ranger/ranger/wiki), and some plug-in in the [Plugins section](https://github.com/ranger/ranger/wiki/Plugins).
Here,giving some common Keybindings,The detalis start with the [following](https://github.com/ranger/ranger/wiki/Official-User-Guide).
* **q** quit ranger
* **Shift + s** -------------quit ranger,and into path previewed with ranger
* **z + h / ctrl + c** ------show hidden files 
* **r + 2** ------------------to run file using python
* **[ and ]** ---------------adjust parent directory
* **g + alphabet** -------enter specified directory
* **o + alphabet** ------directory sort,such as ,o+c is sort by time,o+n is sort by name
* **/** -----------------------search file like vim
* **z + f** ------------------search file by keyword 
* **y + p** -----------------copy path of file
* **y + n** -----------------copy name of file
* **y + .** ------------------copy name of file remove suffix
* **s** ---------------------- call shell
* **c + w** -----------------rename 
* **a** ----------------------rename
* **shift + a** ------------rename in the end of the name
* **v** ----------------------all selected
* **space** ----------------select a file
* **:bulkrename** ------bulkrename using vim
* **yy** --------------------copy file
* **pp** --------------------paste file
* **po** --------------------paste file to cover other file 
* **dd** --------------------cut file
* **dD** --------------------delete file
* **ud/y** -----------------cancel cut/copy
* **du** ---------------------view size of file
* **w** ---------------------open manager
* **:compress + newname** ------compress file
* **yy + shift + x** ------decompression
#### **2.4 Configuration files of ranger** 
Ranger can automatically copy default configuration files to **~/.config/ranger** if you run it with the switch 

```sh
$ ranger --copy-config=all 
$ export RANGER_LOAD_DEFAULT_RC=FALSE
```

After,you can see four files in your directory **~/.config/ranger** 

```sh
rc.conf         #-is used for setting various options and binding keys to functions.
commands.py     #-contains various functions' implementation, written in Python,used to modify |ranger's| behavior, 
                # and implement your own [Custom Commands](https://github.com/ranger/ranger/wiki/Custom-Commands).
rifle.conf      #-decides which program to use for opening a file.
scope.sh        #-is a shell script used to generate previews for various file types.

```
## <h2 id="3"> 3.Neovim[^](#0) </h2>
#### **3.1 Introduction of Neovim:**
&emsp;**[Neovim](http://neovim.io/)** is a refactor, and sometimes redactor, in the tradition of Vim (which itself derives from Stevie). It is not a rewrite but a continuation and extension of Vim. Many clones and derivatives exist, some very clever—but none are Vim. Neovim is built for users who want the good parts of Vim, and more. 

---
#### **3.2 Install Neovim:** 
Since 18.04 via official repository As in Debian,Neovim is in [Ubuntu](https://packages.ubuntu.com/search?keywords=neovim)
```sh
$ sudo apt install neovim
```
---
#### **3.3 Configuration of Neovim:** 
Here,some basic Keybindings be gived:
* **w/b,j/k and l/h** -------------control direction of cursor in normal mode  
* **yy | p or shift+p** ------------copy all of line | paste in next line,or paste in last line
* **dd** ------------------------------delete all of line,after,however,key **p or shift+p** will paste words in next/last line
* **u** --------------------------------withdraw last operation
* **shift+v+directionKey** -----Select some words according to all of line
* **v+directionKey** -------------Select some words according to single word,after you can **yy or dd** words that are selected.
* **Esc,Ctrl+c or Ctrl+[** --------quit insert mode
* **d + directionKey** -------------delete words accroding to direction-Key
--- 
* **o or shift+o** ------------------into Insert mode and you can to write in next/last line
* **a or shift+a** ------------------cursor forward one point or in end into Insert mode 
* **i or shift+i** --------------------into Insert mode or cursor to the beginning of line and into Insert mode
* **/ + words** ---------------------search the words
* **n/N or * / #** -------------------view words searched both up and down[
* **"+y**-------------------------------copying the contents to your clipboard
---

![vim-help1](/home/life/下载/vim-help1.jpg)
![vim-help2](/home/life/下载/vim-help2.jpg)

---
#### **3.4 Configuration files of Neovim:** 
First,different between vim and neovim.
* Configuration files of vim in **~/.vim/vimcr** 
* Configuration files of neovim in **~/.config/nvim/init.vim** 

you can setting your-self (neo)vim through to adjust **init.vim** .
```vim
:PlugInstall
:CheckHealth
:MakedownPreview #keybindings is seted "r"
```
**First Important** is Install useful plug-in for your-self (neo)vim.
#### **3.5 useful plug-in:** 
first you need manger your plug-in,so we Install [vim-plug](https://github.com/junegunn/vim-plug)

Here, giving some plug-in of neovim
* [markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim)
* [vim-table-mode](https://github.com/dhruvasagar/vim-table-mode)
* [nerdtree](https://github.com/preservim/nerdtree)
* [coc.nvim](https://github.com/neoclide/coc.nvim)
---
Here,giving some keybindings in coc.nvim or other plug-in
* **tt** -------------------you can view directory in neovim
* **ctrl + o** ----------- back cursor to last adjust
* **ctrl + i** -------------back cursor to next adjust
* **g + f** ---------------if cursor on a path of file,keying g+f can coming The file.ctrl+o can back last file 
* **:normal A some words** ----------to adjust all of the words selected
* **:r !figlet words** -------drawing the words using ---
* **:%TOhtml** --------input file become .html
* **\<LEADER> + -/=** --------code error using \<LEADER> + -/= to find. My \<LEADER> of key is \
---
Markdown keybindings
![markdown](/home/life/下载/markdown.png)
---
Install [coc-plugin](www.github.com/neoclide/coc.nvim/wiki/Using-coc-extensions)
:you can into init.vim and key
```
$ CocInstall plugin-name
```
##4
## <h2 id="4"> 4.GitHub[^](#0) </h2>
#### **4.1 Introduction:** 
#### **4.3 Configuration of GitHub:** 
Here,some basic Keybindings be gived:
* **git init** ---------------------------------------Initialized empty Git repository in your path of folder.
* **git status** ----------------------------------to view the current status.
* **git add ./name of files** -----------------all of files or several files added to commit.
* **git diff** --------------------------------------to tell you something of changes but not added to commit.
* **git reset /or add name of files** ------withdraw commit to all of files or several files
* **git config --global user.name "Li Zhikai"** --------------to tell git a name of buddy who have been commit.
* **git config --global user.email "lzk170@163.com"** ----------to tell git a email of buddy who have been commit.
* **git config --global core.editor emacs**-------------------------- to adjust editor
* **git commit -m "describtion of your changes"** --------------commit files
* **git commit** --------------------------------- commit files and into vim to edit describtion of your changes if you have a file that not committed yet.  
* **vim .gitignore** -----------------------------into .gitignore to edit some files you would like to commit and don't to see with anybody.first,edit name files into .gitignore.sectond,git add .gitignore and git commit -m "add gitignore"
* **git rm --cached name of files** -----------------something you need to note: if git start trace a file, you need first stop(useing this commend).if you want replace it to .gitignore.
* **git branch name** ------------------------creating branch
* **git checkout name** ---------------------switch branch
* **git merge name** -------------------------merge branch
* **git branch -d name** --------------------remove branch
* **git remote set-url origin https://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@github.com/ZhikaiLi2022/notes.git** ---------------into a projects
    git remote add origin https://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@github.com/ZhikaiLi2022/notes.git
    git remote -v
* **git push -u origin master** --------------------------------Signe in as ZhikaiLi2022
    git push --set-upstream origin master
* **git config credential.helper store** ---------------------------------------store user informeantion
* **git log** show up log
