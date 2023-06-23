#!/usr/bin/env python
# coding: utf-8

# ```{math}
# 
#     \DeclareMathOperator*{\argmin}{arg\,min}
# ```

# # Notebook use continued
# 
# Note, even though this is a new section in a chapter, we still use the single `#` for the title of the Notebook, rather than the next level `##`.
# 
# For each new Notebook, we need to 
# 
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ## Admonitions
# 
# Jupyter Book uses an extended set of commands to standard Markdown. This extension is called MyST (Markedly Structured Text) and have some rather nice features. Unfortunately, they can only be seen in the final book, but look slighty ungainly in the Notebook itself.
# 
# One feature is admonitions, which are things like warning, notes, etc.
# 
# The general syntax is 
# 
#     ```{admonition_name}
#     Text
#     ```
# 
# ```{Note}
# This is a note
# ```
# 
# ```{warning}
# Here is a warning
# ```
# 
# ```{tip}
# Here is a tip
# ```
# 
# Alternatively, a heading can be given to the admonition using the syntax
# 
#     ```{admonition_name} Title
#     Text
#     ```
# 
# ```{Note} Note title
# This is a note
# ```
# 
# ```{danger}Danger Danger Will Robinson!
# This is dangerous
# ```
# 
# 
# 
# The full list of admonitions is
# 
# ```{admonition} Extra Credit
# Some stuff
# ```
# 
# ```{admonition} Theorem 10
# Some more stuff 
# ```
# 
# 
# 
# :::{remark}
# Test this other type of fencing
# :::
# 
# :::{admonition} Testing the colon fencing
# Test
# :::

# [First Notebook](./notebook1.ipynb)

# Try adding a figure, but don't show the code that produces it (check out Cell Metadata). Here remove-input has been used, but hide-input allows the code to be uncovered if desired. 

# In[2]:


x = np.linspace(0,1,100)
y = x**2
fig = plt.plot(x,y)


# ## A subheading
# 
# <div class="command"> blah </div>
# 
# <div class="test"> blah </div>
# 
# <div class="theorem"> 
#     <p class="caption"> Theorem Name </p>
#     <p> Picking up a theorem environment from the style file.</p> 
#     <p> Markdown Maths doesn't seem to get picked up in these environments. </p>
#     <p> Perhaps we gave to use proper html syntax? </p>
#     <span class="math notranslate nohighlight">\(a+b = 2\)</span>
#     $$a+b=2$$
# </div>
# 
# <div class="example">
#     <p> Picking up an example environment from the style file.  </p>
# </div>

# ```{Note}
# This is a note, does it work?
# 
# It is picking up the note environment from the style file
# ```
# 
# ```{admonition} Extra Credit
# Some stuff
# ```
# 
# ```{admonition} Theorem 10
# Some more stuff 
# ```
# 
# ```{warning}
# Here is a warning
# ```
# 
# ```{tip}
# Here is a tip
# ```
# 
# :::{remark}
# Test this other type of fencing
# :::
# 
# :::{admonition} Testing the colon fencing
# Test
# :::
# 
# 
# Let's try and pick up a LaTeX macro from the config.yml file. They should be defined in this position:
# 
# sphinx:
#     mathjax3_config:
#       tex:
#         macros:
# 
# $$\myfrac{1}{2}$$  
# 
# $$\argmax_{x \in X} |x|$$
# 
# $$\partd{f}{x},\quad \partd{f}{y}$$
# 

# ### A sub-subheading

# ## Another subheading
# 
# Adding a theorem - need to include this in config.yml
# sphinx: 
#     extra_extensions:
#         - sphinx_proof
# 
# ````{prf:theorem} Orthogonal-Projection-Theorem
# :label: my-theorem
# 
# Given $y \in \mathbb R^n$ and linear subspace $S \subset \mathbb R^n$,
# there exists a unique solution to the minimization problem
# 
# ```{math}
# :label: eq-label1
# \hat y := \argmin_{z \in S} \|y - z\|
# ```
# 
# $$\hat y := \argmin_{z \in S} \|y - z\|$$(eq-label2)
# 
# The minimizer $\hat y$ is the unique vector in $\mathbb R^n$ that satisfies
# 
# * $\hat y \in S$
# 
# * $y - \hat y \perp S$
# 
# 
# The vector $\hat y$ is called the **orthogonal projection** of $y$ onto $S$.
# ````
# 
# Reference like this: 
# 
# {prf:ref}`my-theorem`
# 
# or this
# 
# {prf:ref}`Orthog Projection <my-theorem>`
# 
# Can also have lemmas, etc
# 
# ```{prf:lemma} Orthogonal-Projection-Theorem
# :label: my-lemma
# 
# $$a+b=c$$ 
# ```
# 
# We can also cross reference to the equations like this: {eq}`eq-label1` and {eq}`eq-label2`
# 
# ```{prf:proof} 
# {prf:ref}`my-theorem`
# 
# Unsurprisngly, we can even add a proof box.
# 
# ```

# Trying out some AMS math stuff
# 
# 
# \begin{align}
# a &= b + c + d \\
# b &= a + c + d
# \end{align}
# 
# 
# 
# $$\begin{pmatrix} a & b & c \\ d & e & f \end{pmatrix}$$

# {eq}`eq-label3` 

# We can emded some dynamic Desmos:
# <iframe src="https://www.desmos.com/calculator/gvtteacngh?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

# Or some Geogebra activities
# <iframe scrolling="no" title="Bisection Algorithm" src="https://www.geogebra.org/material/iframe/id/dwyt7xxx/width/1120/height/463/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1120px" height="463px" style="border:0px;"> </iframe>

# ## Tables
# 
# ```{list-table} Give it a title
# :header-rows: 1
# :name: example-table
# 
# * - Training
#   - Validation
# * - 0
#   - 5
# * - 13720
#   - 2744
# ```
# Then add a label like this {numref}`example-table`
