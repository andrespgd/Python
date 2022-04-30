## Conda for Linux 

- download .sh from Anaconda site

```
chmod 755 Anaconda3-2019.07-Linux-x86_64.sh
./Anaconda3-2019.07-Linux-x86_64.sh
```


## Update
```
conda --version
conda update conda
```


## Create environment

1- create environment
```
conda create -n p310 numpy scipy pandas scikit-learn notebook spyder python=3.10
conda activate p310
conda deactivate
```

2- Check environments
```
conda env list
```
>conda environments:

>base                  *  /home/a1/anaconda3

>py37                     /home/a1/anaconda3/envs/py37


## How to view the path to the conda environment

</br>Linux:
```
source activate python35
echo $CONDA_PREFIX
```

</br>Windows:
```
conda activate python35
echo %CONDA_PREFIX%
```

</br>To show paths to all your environments
```
conda info --envs
```

## install additional packages

1-from env
```
(conda-env) % conda install pandas=0.24.1
```
OR
```
(conda-env) % pip install pandas
```
2-from shell
```
% conda install -n conda-env pandas=0.24.1 
```


## update the packages

1-from env
```
(conda-env) % conda update pandas
```
OR
```
(conda-env) % conda update --all
```
2-from shell
```
% conda update -n conda-env pandas
```


## list the packages 

1-from env
```
(conda-env) % conda list
```
2-from shell
```
% conda list -n conda-env
```

## Setup an existing conda env to PyCharm

[Conda on Pycharm](https://medium.com/infinity-aka-aseem/how-to-setup-pycharm-with-an-anaconda-virtual-environment-already-created-fb927bacbe61)

