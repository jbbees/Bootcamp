# Commands

## Navigation Commands

* pwd               print working directory.
* cd                change directory - *you can change **forward** to a lower directory in the file path.*
* cd ..             change **back** 1 directory higher in the file path. The exact preceding folder.
* cd ../..          change **back** 2 directories higher in file path. 
* cd ../../..       change **back** 3 directories.
* cd ~              change to home directory C:/
* cd D:/            change to another root directory. In this case the external D:/ drive. 
* dir -r            find files.

*a directory is noted with a slash character **/** at end.*
*putting --help after a command, brings up manual for the command itself.*
*if you press tab while typing change directory, it will add the / at end of line.*

*any directory or file name that has spaces needs a quotation **' '** mark around it.
> cd Folder A    *this will fail because there's a space in object name.*
> cd 'Folder A'  *use quotation marks* 

* pushd             push directory. 

> *file path of foldera/folderb/folderc*
> pushd foldera/
> *user/foldera/*

* popd              pop directory.

* help              brings up a manual page. 
* man               typing man before any command will give you the **manual page** for that command with all the -flags and functions.
> man ls   *list the definition of ls command and all -flags.*

*You can only go back as far as the **root directory**, in this case the **C:/** on your computer.*
C:/ will be displayed as **/** without the letter C. 
*You can only change to directories that already exist. You cannot create a directory using cd command.* 
*C:/ is the root directory of the file path on the computer you're working on.*

* ls                list directory: list everything contained in the current directory.

> ls folder1
> ls folder1/

* ls .*             using an asterisk is a **wild card** in this case the list command looks for anything starting with a period. *good for looking at hidden files.*
* ls M*             wildcard, list all files beginning with capital 'M' 
* ls -a             
* ls -l         
* ls -h
* ls -ltrh          lists all files from newest to oldest. 

> ls folder1       *this will list contents of folder without changing directory.

* dir -r            this will list every directory in the entire file path w/o changing the directory.

File paths have to be followed exactly when changing directories.

### Making directories and files

* mkdir             make an empty folder.
* mkdir -p          makes nested directories.
> mkdir folder1/folder2/folder3   *makes three directories nested within eachother. folder1 is parent*

* touch             make an empty file object. *Use an extension like .txt after file name to make it a text file.*

> mkdir folder1    *creates an empty folder.*
> touch file.txt   *creates an empty text file called file.txt*
> touch file       *creates a file called file, but since no extension after object name it creates a wonky un-openable file.*

> touch folder1/file.txt   *creates file.txt inside folder1 without having to change to folder1 directory.*

#### Removing directories 

* rmdir             remove directory. removes the folder as long it is **empty**. If there are folders/files hosted inside folder. rmdir will not work. 

*rmdir only works on empty folders*
*you cannot remove the folder when you are in the folder itself.* 
*you have to be in the preceding hosting directory/folder to delete the folder.* 

* rm                remove command. only removes files, not folders. 

> rm file.txt/folder1   *this removes the file from the folder without having to change directory.*

* rm -r             removes directories recursively. deletes all files in a folder. you can run this on a folder. it will not delete the folder only all files in it.
> rm -r folder1/        *keep folder1, delete everything stored in it.*

**DANGEROUS REMOVE COMMANDS - BEWARE! PRANKSTERS FOOL PEOPLE TO TYPING THESE** 

* rm -r/            remove every directory under root directory C:/   *this will trigger a warning from Windows.*
* rm -rf/           removes every directory under the C:/ drive by force.  **absolute worst. it forces the remove action, no trigger warning. cannot be prevented.**

##### Renaming objects, Move Command.

* mv                move command. renames folders and files. you are moving the object into a new name.

> mv folder1 folder2           *renames folder1 as folder2.*
> mv file.txt newfile.txt      *this simply changes the name to newfile.txt. File remains in folder.*

*The folder or file has to exist to rename it.*
*You cannot rename folders or files to names that **already exist** on other objects of the same **object-type** in the hosting folder. All object names MUST BE unique.*
*You cannot rename folders when you are in the folder. You have to be in the hosting folder*

* mv                move command. also moves objects from one directory to another. it not copying the object. the original directory will no longer have the object.

*moving moves the folder and any folders/files contained in that folder.*

> mv newfile.txt folder2    *moves the newfile.txt into folder2 directory. host folder no longer has file.*

*NOTE: You cannot move objects from one root directory to another. Cannot move from C:/ drive to D:/* 

##### Copying

* cp                copy function. works on folders and files. 

*syntax: cp source destination*
*copying a file creates the file, so desination object doesn't have to exist first.* 

> cp file1.txt file2.txt  *copies file1.txt and makes a copy in the same folder called file2.txt* 
> cp file1.txt folder2/   *copies file1.txt into folder2 directory.*

* cp -r             copy recursive;y. This copies the folder and every object contained in the folder.

* robocopy 

###### Echo,Cat,Stream a File,Explorer commands

* echo              echoes what you typed in back to the command line.   

*echo can be used to write data to files that exist.*
*echo "text" file1.txt  make sure to enclose quotations " " on text you want."

> echo "new text being inserted into file1. this will overwrite" file1.txt   
*this will insert text into the file, but it will overwrite whatever is written in the file.*  

*echo can also created files that do not exist and insert text into them.*

> echo "Creating new file with text" > file2.txt

* cat               concatenate. echoes back the contents of a file back to command line. **does not work on folders**. 
> cat file1.txt        *displays what is in file.* 

*if the file is empty, cat will return nothing.*

* less              this also displays file contents infiite loop. crashes the command line.
* more              streams the file.

* explorer          opens the folder or file 
> explorer file1.txt     *open the file.*

###### Other useful commands

* hostname          my computer's network name. 
* ipconfig          checks if connected to internet. doesn't display the router name. 
* ipconfig /release disconnect from internet. 
* clear             clears the screen. 
* code              opens a file in VS code  *need VS code installed for this to work.*
* kill              kills the the current bash session.
* python -V         displays what version of python you're using. 

###### Advanced commands 

* forefiles         run a command on batches of files. 
* attrib
* icalcs
* runas             become a super root user. 

###### Git-Hub commans

* git clone
* git pull 
* git status
* git init
* git add .
* git commit -m "comments"
* git push  

###### SSH Keys (Git-Hub)
*ssh means secure shell*

* ssh-keygen -t rsa -b 4096 -C "example@email.com"      creates a public/private rsa key-pair
> Enter the file in which to save they key? *Hit enter. This will create a default .ssh/ directory.* 
> Overwrite? *Yes*
> Enter passphrase. *Hit enter. If you do enter a passphrase it's invisible when you type it in.*
> Re-enter passphrase. *Hit enter*

* ssh-agent       checks if the ssh agent service is turned on. *If 

##### Anaconda Commands

* conda update conda
* conda update anaconda
* conda create -n 
* conda activate dev
* jupyter lab 