# Conda for Linux 

1- download .sh from Anaconda site

2-
chmod 755 Anaconda3-2019.07-Linux-x86_64.sh

3-
./Anaconda3-2019.07-Linux-x86_64.sh
>will install ./anaconda3/bin/conda

# update Conda

conda --version

conda update conda



# create a python3.7 environment

1- create environment
conda create -n p37 numpy scipy pandas scikit-learn notebook spyder

2-
conda activate p37
conda deactivate

3-
conda env list
>conda environments:

>base                  *  /home/a1/anaconda3

>py37                     /home/a1/anaconda3/envs/py37


## install additional packages

1-from env

(conda-env) % conda install pandas=0.24.1

OR

(conda-env) % pip install pandas

2-from shell

% conda install -n conda-env pandas=0.24.1 



## update the packages

1-from env

(conda-env) % conda update pandas

OR

(conda-env) % conda update --all

2-from shell

% conda update -n conda-env pandas



## list the packages 

1-from env

(conda-env) % conda list

2-from shell

% conda list -n conda-env



# NOTES

-Whereas pip only installs Python packages from PyPI, conda can both

    Install packages (written in any language) from repositories like Anaconda Repository and Anaconda Cloud.
    Install packages from PyPI by using pip in an active Conda environment.
