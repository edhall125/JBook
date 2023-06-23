# Jupyter Book Installation

```{note}
If you don't already have a Python/Jupyter Notebook installation on your computer, then the simplest way to obtain it is by installing Anaconda from this link: [Anaconda](https://www.anaconda.com/download)

Jupyter notebooks can then be opened through the Anaconda Navigator, or directly through a terminal/Anaconda prompt using the command:

> `jupyter notebook name_of_file.ipynb`

```

## Using Anaconda to install Jupyter Books

```{note}
We will assume you are using Anaconda to install the packages, although many of them can also be installed using pip. The following should work on Windows from an Anaconda prompt or from a terminal in Mac/Linux.
```

We recommend you set up a special environment with conda to ensure you don't break anything with your current setup. From the terminal/Anaconda prompt, type:

> `conda create --name JBook python`

Or replace JBook with whichever environment name you want. You should answer 'y' to install new packages.

Now, activate that environment using

> `conda activate JBook`

You will probably need to install any Python packages you need in this environment. For the demonstration, you will need NumPy and Matplotlib. Again, answer 'y' to install new packages.

> `conda install -c conda-forge numpy`

> `conda install -c conda-forge matplotlib`

To install the Jupyter book package, type

> `conda install -c conda-forge jupyter-book`

We also need to install the sphinx-proof package, which unfortunately needs to be done using pip, so type this:

> `pip install sphinx-proof`

We might also like to ensure the Jupyter Notebooks can run R code as well. To do this, we can install R and the R kernel:

>  `conda install -c r r`
>  `conda install -c r r-irkernel`

Now, from the terminal, open an R console by typing:

> r

Then run the following two commands

> `install.packages('IRkernel')`
> `IRkernel::installspec()`

Finally quit R with 

> `q()`