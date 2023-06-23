#!/usr/bin/env python
# coding: utf-8

# # Simple Notebook Use
# 
# There are essentialy two components to a Jupyter Notebook:
# 
# * Markdown blocks
# * Code blocks
# 
# ## Markdown blocks
# 
# A markdown block has essentially the same functionality as one in RMarkdown.
# 
# To add a title/subtitle/etc in a block, use `#`, `##`, etc, followed by a name, for example, above we have `# Simple Notebook Use` and `## Markdown blocks`. Later we will see how to create a link back to a section in the same/different file.
# 
# A line break can be created using `---`:
# 
# ---
# 
# * Text can be made bold by using this syntax: `**this text is bold**`: **this text is bold**
# * Text can be put in italics by using this syntax: `*this text is in italics*`: *this text is in italics*
# 
# ---
# 
# Lists without numbers can be created with repeated use of `*` (or `-` or `+`), see the example below
# 
# * First item
# * Second item
#     * subitem
#         * subsubitem
# * third item
# 
# Enumerated lists can be created using `1.`, `2.`, etc:
# 
# 1. First item
# 2. Second item
# 3. subitem
# 
# or even by just repeating `1.`
# 
# 1. First item
# 1. Second item
# 1. third item
# 
# Starting the numbering from another value is also possible too:
# 
# 20. First item
# 1. Second item
# 1. third item
# 
# ---
# 
# If you wish to write some Python inline (and for it not to be executed), put the code within backticks `a+b`. This is also useful for writing things verbatim.
# 
# To make a quoute that appears in a box, use `>`
# 
# > Here is a quote
# 

# ## Code blocks
# 
# A code block can be used to enter and run Python code (or R or Julia). If the final line produces just some output this is printed to the screen

# In[1]:


1+1
2+2


# If the final line creates a variable, then this is not printed to the screen. The `print()` command can be used instead. Note, variables can be used elsewhere in the Notebook once the code block they are in has been run.

# In[2]:


a = 10
print(a)


# Functions can be defined and used as well

# In[3]:


def add_two(x):
    return(x+2)

add_two(8)


# Modules can also be imported and used

# In[4]:


import numpy as np
np.array([[1,2,3],[2,3,4]])


# Note, a simple way to inspect the variables in a Jupyter Notebook is to type `%whos` in a  code block

# In[5]:


get_ipython().run_line_magic('whos', '')


# [Second Notebook](notebook2.ipynb)

# Can we reference something from somewhere else? {prf:ref}`Orthog Projection <my-theorem>`
