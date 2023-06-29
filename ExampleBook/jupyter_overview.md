# Jupyter Book Overview

A Jupyter Book is essentially a collection of Jupyter Notebooks (or other Markdown files) compiled together in an HTML format. Far more information about Jupyter Books can be found [here](https://jupyterbook.org/en/stable/intro.html)

There are two `.yml` files that control the Jupyter Book:

* `_config.yml` - the configuration file
* `_toc.yml` - the table of contents file

See the example files in the `ExampleBook/` folder. Note, files selected in `_toc.yml` do not need to have an extension - `.ipynb` and Markdown files (`.md`/`.Rmd`) are automatically searched for. 

```{Note}
Extra styling can be incorporated using a `.css` file inside the `_static` folder. There shouldn't really be any need to edit this file.
```

(compilation)= 
## Compiling a Book

Compilation of a Jupyter book is done at an Anaconda Prompt/terminal and from the folder directly above the top level folder where the files are stored. Hence, to compile this example book, first navigate to the `JBook` folder created by unzipping `JBook.zip`. You can used the `cd` command to change directories.

The simplest syntax to use for compilation is

> `jupyter-book build folder_name`

So, to compile this book, use `jupyter-book build ExampleBook`. 

The above checks whether any markdown style files have recently been changed and will not recompile these files if they have not been. Hence, sometimes the book will not recompile, especially if the `.yml` files are the only ones to have been changed. To enforce compilation of all files, use:

> `jupyter-book build --all folder_name`

Other options can be used, but are not detailed here.

## Viewing the Book

After compilation, navigate to `ExampleBook\_build\html` and open `main.html` in a web browser.

```{note}
It might say to open `ExampleBook\_build\html\index.html`, but doing this appears to not always work.
```