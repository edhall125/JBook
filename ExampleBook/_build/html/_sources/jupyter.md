# Jupyter Book Installation

## Installation

```{note}
If you don't already have a Python/Jupyter Notebook installation on your computer, then the simplest way to obtain it is by installing Anaconda from this link: [Anaconda](https://www.anaconda.com/download)

Jupyter notebooks can then be opened through the Anaconda Navigator, or directly through a terminal/Anaconda prompt using the command:

> jupyter notebook name_of_file.ipynb

```

### Using Anaconda to install Jupyter Books

```{note}
We will assume you are using Anaconda to install the packages, although many of them can also be installed using pip. The following should work on Windows from an Anaconda prompt or fomr a terminal in Mac/Linux.
```

We recommend you set up a special environment with conda to ensure you don't break anything with your current setup. From the terminal/Anaconda prompt, type:

> conda create --name JBook python

Or replace JBook with whichever environment name you want.

Now, activate that environment using

> conda activate JBook

You will probably need to install any Python packages you need in this environment. For the demonstration, you will need NumPy and Matplotlib

> conda install -c conda-forge numpy

> conda install -c conda-forge matplotlib

To install the Jupyter book package, type

> conda install -c conda-forge jupyter-book

We also need to install the sphinx-proof package, which unfortunately needs to be done using pip, so type this:

> pip install sphinx-proof

We might also like to ensure the Jupyter Notebooks can run R code as well. To do this, we can install the R kernel:

>  conda install -c r r-irkernel

Finally, we might need to use the Jupytext package to allow RMarkdown files to be used as well. To install this, do

> conda install jupytext

## Overview

A Jupyter Book is essentially a collection of Jupyter Notebooks (or other Markdown files) in an HTML format.

There are two `.yml` files that control the Jupyter Book:

* `_config.yml` - the configuration file
* `_toc.yml` - the table of contents file

See the example files in the `ExampleBook/` folder.

By default, all subfolders are searched for possible Jupyter Notebooks (`.ipynb`) and Markdown files (`.md`/`.Rmd`). 

```{Note}
Extra styling can be incorporated using a `.css` file inside the `_static` folder. There shouldn't really be any need to edit this file.
```

