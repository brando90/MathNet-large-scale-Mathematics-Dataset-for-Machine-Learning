To install the framework I would suggest to download the code. One easy way is to git clone it:

    git clone git@github.com:brando90/eit_proj1.git

Once you have that use pip to run setup.py to install the library:

    pip install main_proj_lib/setup.py

or go to the directory where setup is. Every time you update the main library you will have *re-install** the framework.

To avoid that I recommend you to go to your terminal and cd to the main_proj_lib:

    cd <path_to_framework_code>/eit_proj1/main_proj_lib

then there use the following to install the library:

    python setup.py develop

this will allow you to use the library code without having to re-installing it. Only use this if you plan to change the main framework code or if you git pull frequently from the changes we make.

Also, its highly recommended that you use virtual environments when installing stuff in python. If you don't know what that means read the following:

http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/

or

https://conda.io/docs/intro.html

and now that you know what they are use `virtualenv` or `conda`.
