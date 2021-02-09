# Running pip

pip is a command line program. When you install pip, a pip command is added to your system, which 
can be run from the command prompt as follows:

for Unix/macOS:

```python -m pip <pip arguments>```

or:

```python3 -m pip <pip arguments>```

```python -m pip``` executes pip using the Python interpreter you specified as python. So ```/usr/bin
/python3.7 -m pip``` means you are executing pip for your interpreter located at /usr/bin/python3.7.

for Windows:

```py -m pip <pip arguments>```

```py -m pip``` executes pip using the latest Python interpreter you have installed. For more details, read the [Python Windows launcher](https://docs.python.org/3/using/windows.html#launcher) docs.

# Installing packages

pip supports installing from [PyPI](https://pypi.org/), version control, local projects, and directly from distribution files.

The most common scenario is to install from [PyPI](https://pypi.org/) using [Requirement Specifiers](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers)

Unix/macOS:
```
python -m pip install SomePackage            # latest version
python -m pip install SomePackage==1.0.4     # specific version
python -m pip install 'SomePackage>=1.0.4'     # minimum version
```

or:
```
python3 -m pip install SomePackage            # latest version
python3 -m pip install SomePackage==1.0.4     # specific version
python3 -m pip install 'SomePackage>=1.0.4'     # minimum version
```

Windows:
```
py -m pip install SomePackage            # latest version
py -m pip install SomePackage==1.0.4     # specific version
py -m pip install 'SomePackage>=1.0.4'     # minimum version
```

For more information and examples, see the [pip install](https://pip.pypa.io/en/stable/reference/pip_install/#pip-install) reference.

# Basic Authentication Credentials

pip supports basic authentication credentials. Basically, in the URL there is a username and password 
separated by ```:```.

```https://[username[:password]@]pypi.company.com/simple```

Certain special characters are not valid in the authentication part of URLs. If the user or password part 
of your login credentials contain any of the special characters [here](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters) then they must be percent-encoded. 
For example, for a user with username “user” and password “he//o” accessing a repository at 
pypi.company.com, the index URL with credentials would look like:

```https://user:he%2F%2Fo@pypi.company.com```

Support for percent-encoded authentication in index URLs was added in pip 10.0.0 (in [#3236](https://github.com/pypa/pip/issues/3236)). Users 
that must use authentication for their Python repository on systems with older pip versions should make 
the latest get-pip.py available in their environment to bootstrap pip to a recent-enough version.

For indexes that only require single-part authentication tokens, provide the token as the “username” and 
do not provide a password, for example -

```https://0123456789abcdef@pypi.company.com```

<h3>netrc Support</h3>

If no credentials are part of the URL, pip will attempt to get authentication credentials for the URL’s 
hostname from the user’s .netrc file. This behaviour comes from the underlying use of [requests](https://requests.readthedocs.io/en/master/user/authentication/#netrc-authentication) which in
turn delegates it to the [Python standard library](https://docs.python.org/3/library/netrc.html).

The .netrc file contains login and initialization information used by the auto-login process. It resides in 
the user’s home directory. The .netrc file format is simple. You specify lines with a machine name and 
follow that with lines for the login and password that are associated with that machine. Machine name is 
the hostname in your URL.

An example .netrc for the host example.com with a user named ‘daniel’, using the password ‘qwerty’ 
would look like:
    
```
machine example.com
login daniel
password qwerty
```

As mentioned in the [standard library docs](https://docs.python.org/3/library/netrc.html), only ASCII characters are allowed. Whitespace and non-
printable characters are not allowed in passwords.

<h3>Keyring Support</h3>

pip also supports credentials stored in your keyring using the [keyring](https://pypi.org/project/keyring/) library. Note that ```keyring``` will need 
to be installed separately, as pip does not come with it included.

```
pip install keyring
echo your-password | keyring set pypi.company.com your-username
pip install your-package --extra-index-url https://pypi.company.com/
```

# Using a Proxy Server

When installing packages from [PyPI](https://pypi.org/), pip requires internet access, which in many corporate 
environments requires an outbound HTTP proxy server.

pip can be configured to connect through a proxy server in various ways:

* using the ```--proxy``` command-line option to specify a proxy in the form 

```[user:passwd@]proxy.server:port```

* using ```proxy``` in a [Config file](https://pip.pypa.io/en/stable/user_guide/#config-file)

* by setting the standard environment-variables ```http_proxy```, ```https_proxy``` and ```no_proxy```.

* using the environment variable ```PIP_USER_AGENT_USER_DATA``` to include a JSON-encoded string in the 

user-agent variable used in pip’s requests.

# Requirements Files

“Requirements files” are files containing a list of items to be installed using [pip install](https://pip.pypa.io/en/stable/reference/pip_install/#pip-install) like so:

Unix/macOS:
python -m pip install -r requirements.txt

Windows:
py -m pip install -r requirements.txt

Details on the format of the files are here: [Requirements File Format](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)

Logically, a Requirements file is just a list of [pip install](https://pip.pypa.io/en/stable/reference/pip_install/#pip-install) arguments placed in a file. Note that you should 
not rely on the items in the file being installed by pip in any particular order.

1. Requirements files are used to hold the result from [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/#pip-freeze) for the purpose of achieving
[repeatable installations](https://pip.pypa.io/en/stable/user_guide/#repeatability)
    In this case, your requirement file contains a pinned version of everything that was
   installed when ```pip freeze``` was run.
   
Unix/macOS:
```
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

Windows:
```
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt
```

2. Requirements files are used to force pip to properly resolve dependencies. pip 20.2 and earlier
[doesn’t have true dependency resolution](https://github.com/pypa/pip/issues/988), but instead simply uses the first specification it finds for a 
   project. E.g. if ```pkg1``` requires ```pkg3>=1.0``` and ```pkg2``` requires ```pkg3>=1.0,<=2.0```, and if ```pkg1``` is resolved
   first, pip will only use ```pkg3>=1.0```, and could easily end up installing a version of ```pkg3``` that conflicts 
   with the needs of ```pkg2```. To solve this problem, you can place ```pkg3>=1.0,<=2.0``` (i.e. the correct 
   specification) into your requirements file directly along with the other top level requirements. Like so:
   
```
pkg1
pkg2
pkg3>=1.0,<=2.0
```

3. Requirements files are used to force pip to install an alternate version of a sub-dependency. For 
   example, suppose ```ProjectA``` in your requirements file requires ```ProjectB```, but the latest version (v1.3) 
   has a bug, you can force pip to accept earlier versions like so:
   
```
ProjectA
ProjectB<1.3
```

4. Requirements files are used to override a dependency with a local patch that lives in version control. 
   For example, suppose a dependency ```SomeDependency``` from PyPI has a bug, and you can’t wait for an 
   upstream fix. You could clone/copy the src, make the fix, and place it in VCS with the tag ```sometag```. 
   You’d reference it in your requirements file with a line like so:
   
```git+https://myvcs.com/some_dependency@sometag#egg=SomeDependency```

If ```SomeDependency``` was previously a top-level requirement in your requirements file, then **replace** that 
line with the new line. If ```SomeDependency``` is a sub-dependency, then **add** the new line.

It’s important to be clear that pip determines package dependencies using [install_requires metadata](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies), not 
by discovering ```requirements.txt``` files embedded in projects.

See also:

* [Requirements File Format](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)

* [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/#pip-freeze)

* [“setup.py vs requirements.txt” (an article by Donald Stufft)](https://caremad.io/posts/2013/07/setup-vs-requirement/)

# Constraints Files

Constraints files are requirements files that only control which version of a requirement is installed, not 
whether it is installed or not. Their syntax and contents is nearly identical to [Requirements Files](https://pip.pypa.io/en/stable/user_guide/#requirements-files). There 
is one key difference: Including a package in a constraints file does not trigger installation of the 
package.

Use a constraints file like so:

Unix/macOS:

`python -m pip install -c constraints.txt`

Windows:

`py -m pip install -c constraints.txt`

Constraints files are used for exactly the same reason as requirements files when you don’t know 
exactly what things you want to install. For instance, say that the “helloworld” package doesn’t work in 
your environment, so you have a local patched version. Some things you install depend on “helloworld”, 
and some don’t.

One way to ensure that the patched version is used consistently is to manually audit the dependencies 
of everything you install, and if “helloworld” is present, write a requirements file to use when installing 
that thing.

Constraints files offer a better way: write a single constraints file for your organisation and use that 
everywhere. If the thing being installed requires “helloworld” to be installed, your fixed version specified 
in your constraints file will be used.

Constraints file support was added in pip 7.1. In [Changes to the pip dependency resolver in 20.3 (2020)](https://pip.pypa.io/en/stable/user_guide/#resolver-changes-2020) 
we did a fairly comprehensive overhaul, removing several undocumented and unsupported quirks from 
the previous implementation, and stripped constraints files down to being purely a way to specify global 
(version) limits for packages.

# Installing from Wheels

“Wheel” is a built, archive format that can greatly speed installation compared to building and installing 
from source archives. For more information, see the [Wheel docs](https://wheel.readthedocs.io/en/stable/) , [PEP 427](https://www.python.org/dev/peps/pep-0427/), and [PEP 425](https://www.python.org/dev/peps/pep-0425/).

pip prefers Wheels where they are available. To disable this, use the [--no-binary](https://pip.pypa.io/en/stable/reference/pip_install/#install-no-binary) flag for [pip install](https://pip.pypa.io/en/stable/reference/pip_install/#pip-install).

If no satisfactory wheels are found, pip will default to finding source archives.

To install directly from a wheel archive:

Unix/macOS:

`python -m pip install SomePackage-1.0-py2.py3-none-any.whl`

Windows:

`py -m pip install SomePackage-1.0-py2.py3-none-any.whl`

For the cases where wheels are not available, pip offers [pip wheel](https://pip.pypa.io/en/stable/reference/pip_wheel/#pip-wheel) as a convenience, to build wheels for 
all your requirements and dependencies.

[pip wheel](https://pip.pypa.io/en/stable/reference/pip_wheel/#pip-wheel) requires the [wheel package](https://pypi.org/project/wheel/) to be installed, which provides the “bdist_wheel” setuptools 
extension that it uses.

To build wheels for your requirements and all their dependencies to a local directory:

Unix/macOS:

```
python -m pip install wheel
python -m pip wheel --wheel-dir=/local/wheels -r requirements.txt
```

Windows:

```
py -m pip install wheel
py -m pip wheel --wheel-dir=/local/wheels -r requirements.txt
```

And _then_ to install those requirements just using your local directory of wheels (and not from PyPI):

Unix/macOS:

```
python -m pip install --no-index --find-links=/local/wheels -r requirements.txt
```

Windows:

```
py -m pip install --no-index --find-links=/local/wheels -r requirements.txt
```

# Uninstalling Packages

pip is able to uninstall most packages like so:

Unix/macOS:

```
python -m pip uninstall SomePackage
```

Windows:

```
py -m pip uninstall SomePackage
```

pip also performs an automatic uninstall of an old version of a package before upgrading to a newer 
version.

For more information and examples, see the [pip uninstall](https://pip.pypa.io/en/stable/reference/pip_uninstall/#pip-uninstall) reference.

# Listing packages

To list installed packages:

Unix/macOS:

```
$ python -m pip list
docutils (0.9.1)
Jinja2 (2.6)
Pygments (1.5)
Sphinx (1.1.2)
```

Windows:

```
C:\> py -m pip list
docutils (0.9.1)
Jinja2 (2.6)
Pygments (1.5)
Sphinx (1.1.2)
```

To list outdated packages, and show the latest version available:

Unix/macOS:

```
$ python -m pip list --outdated
docutils (Current: 0.9.1 Latest: 0.10)
Sphinx (Current: 1.1.2 Latest: 1.1.3)
```

Windows:

```
C:\> py -m pip list --outdated
docutils (Current: 0.9.1 Latest: 0.10)
Sphinx (Current: 1.1.2 Latest: 1.1.3)
```

To show details about an installed package:

Unix/macOS:

```
$ python -m pip show sphinx
---
Name: Sphinx
Version: 1.1.3
Location: /my/env/lib/pythonx.x/site-packages
Requires: Pygments, Jinja2, docutils
```

Windows:

```
C:\> py -m pip show sphinx
---
Name: Sphinx
Version: 1.1.3
Location: /my/env/lib/pythonx.x/site-packages
Requires: Pygments, Jinja2, docutils
```

For more information and examples, see the [pip list](https://pip.pypa.io/en/stable/reference/pip_list/#pip-list) and [pip show](https://pip.pypa.io/en/stable/reference/pip_show/#pip-show) reference pages.

# Searching for Packages

pip can search [PyPI](https://pypi.org/) for packages using the `pip search` command:

Unix/macOS:

`python -m pip search "query"`

Windows:

`py -m pip search "query"`

The query will be used to search the names and summaries of all packages.

For more information and examples, see the [pip search](https://pip.pypa.io/en/stable/reference/pip_search/#pip-search) reference.

# Configuration

<h3>Config file</h3>

pip allows you to set all command line option defaults in a standard ini style config file.

The names and locations of the configuration files vary slightly across platforms. You may have per-
user, per-virtualenv or global (shared amongst all users) configuration:

<h4>Per-User</h4>

* On Unix the default configuration file is: `$HOME/.config/pip/pip.conf` which respects the 
  `XDG_CONFIG_HOME` environment variable.
  
*  On macOS the configuration file is `$HOME/Library/Application Support/pip/pip.conf` if directory 
   `$HOME/Library/Application Support/pip` exists else `$HOME/.config/pip/pip.conf`.
   
* On Windows the configuration file is `%APPDATA%\pip\pip.ini`.

There is also a legacy per-user configuration file which is also respected. To find its location:

* On Unix and macOS the configuration file is: `$HOME/.pip/pip.conf`

* On Windows the configuration file is: `%HOME%\pip\pip.ini`

You can set a custom path location for this config file using the environment variable `PIP_CONFIG_FILE`.

<h4>Inside a virtualenv:</h4>

* On Unix and macOS the file is `$VIRTUAL_ENV/pip.conf`

* On Windows the file is: `%VIRTUAL_ENV%\pip.ini`

<h4>Global:</h4>

* On Unix the file may be located in `/etc/pip.conf`. Alternatively it may be in a “pip” subdirectory of 
  any of the paths set in the environment variable `XDG_CONFIG_DIRS` (if it exists), for example `/etc/xdg
  /pip/pip.conf`.
  
* On macOS the file is: `/Library/Application Support/pip/pip.conf`

* On Windows XP the file is: `C:\Documents and Settings\All Users\Application Data\pip\pip.ini`

* On Windows 7 and later the file is hidden, but writeable at `C:\ProgramData\pip\pip.ini`

* Global configuration is not supported on Windows Vista.

The global configuration file is shared by all Python installations.

If multiple configuration files are found by pip then they are combined in the following order:

1. The global file is read
2. The per-user file is read
3. The virtualenv-specific file is read

Each file read overrides any values read from previous files, so if the global timeout is specified in both 
the global file and the per-user file then the latter value will be used.

he names of the settings are derived from the long command line option, e.g. if you want to use a 
different package index (`--index-url`) and set the HTTP timeout (`--default-timeout`) to 60 seconds 
your config file would look like this:

```
[global]
timeout = 60
index-url = https://download.zope.org/ppix
```

Each subcommand can be configured optionally in its own section so that every global setting with the 
same name will be overridden; e.g. decreasing the `timeout` to `10` seconds when running the `freeze` 
([pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/#pip-freeze)) command and using `60` seconds for all other commands is possible with:

```
[global]
timeout = 60

[freeze]
timeout = 10
```

Boolean options like `--ignore-installed` or `--no-dependencies` can be set like this:

```
[install]
ignore-installed = true
no-dependencies = yes
```

To enable the boolean options `--no-compile`, `--no-warn-script-location` and `--no-cache-dir`, falsy 
values have to be used:

```
[global]
no-cache-dir = false

[install]
no-compile = no
no-warn-script-location = false
```

For options which can be repeated like `--verbose` and `--quiet`, a non-negative integer can be used 
to represent the level to be specified:

```
[global]
quiet = 0
verbose = 2
```

It is possible to append values to a section within a configuration file such as the pip.ini file. This is 
applicable to appending options like `--find-links` or `--trusted-host`, which can be written on multiple 
lines:

```
[global]
find-links =
    http://download.example.com

[install]
find-links =
    http://mirror1.example.com
    http://mirror2.example.com

trusted-host =
    mirror1.example.com
    mirror2.example.com
```
This enables users to add additional values in the order of entry for such command line arguments.

<h3>Environment Variables</h3>

pip’s command line options can be set with environment variables using the format 
`PIP_<UPPER_LONG_NAME>` . Dashes (`-`) have to be replaced with underscores (`_`).

For example, to set the default timeout:

Unix/macOS:

`export PIP_DEFAULT_TIMEOUT=60`

Windows:

`set PIP_DEFAULT_TIMEOUT=60`

This is the same as passing the option to pip directly:

Unix/macOS:

`python -m pip --default-timeout=60 [...]`

Windows:

`py -m pip --default-timeout=60 [...]`

For command line options which can be repeated, use a space to separate multiple values. For 
example:

Unix/macOS:

`export PIP_FIND_LINKS="http://mirror1.example.com http://mirror2.example.com"`

Windows:

`set PIP_FIND_LINKS="http://mirror1.example.com http://mirror2.example.com"`

is the same as calling:

Unix/macOS:

`python -m pip install --find-links=http://mirror1.example.com --find-links=http://mirror2.example.com`

Windows:

`py -m pip install --find-links=http://mirror1.example.com --find-links=http://mirror2.example.com`

Options that do not take a value, but can be repeated (such as `--verbose`) can be specified using the 
number of repetitions, so:

`export PIP_VERBOSE=3`

is the same as calling:

`pip install -vvv`

Note:
Environment variables set to be empty string will not be treated as false. Please use `no`, `false` or `0` instead.

<h3>Config Precedence</h3>

Command line options have precedence over environment variables, which have precedence over the 
config file.

Within the config file, command specific sections have precedence over the global section.

Examples:
* `--host=foo` overrides `PIP_HOST=foo`
* `PIP_HOST=foo` overrides a config file with `[global] host = foo`
* A command specific section in the config file `[<command>] host = bar` overrides the option with same 
  name in the `[global]` config file section
  
# Command Completion

pip comes with support for command line completion in bash, zsh and fish.

To setup for bash:

`python -m pip completion --bash >> ~/.profile`

To setup for zsh:

`python -m pip completion --zsh >> ~/.zprofile`

To setup for fish:

`python -m pip completion --fish > ~/.config/fish/completions/pip.fish`

Alternatively, you can use the result of the `completion` command directly with the eval function of your 
shell, e.g. by adding the following to your startup file:

`eval "`pip completion --bash`"`

# Installing from local packages

In some cases, you may want to install from local packages only, with no traffic to PyPI.

First, download the archives that fulfill your requirements:

Unix/macOS:

`python -m pip download --destination-directory DIR -r requirements.txt`

Windows:

`py -m pip download --destination-directory DIR -r requirements.txt`

Note that `pip download` will look in your wheel cache first, before trying to download from PyPI. If you’ve 
never installed your requirements before, you won’t have a wheel cache for those items. In that case, if 
some of your requirements don’t come as wheels from PyPI, and you want wheels, then run this instead:

Unix/macOS:

`python -m pip wheel --wheel-dir DIR -r requirements.txt`

Windows:

`py -m pip wheel --wheel-dir DIR -r requirements.txt`

Then, to install from local only, you’ll be using [--find-links](https://pip.pypa.io/en/stable/reference/pip_install/#install-find-links) and [--no-index](https://pip.pypa.io/en/stable/reference/pip_install/#install-no-index) like so:

Unix/macOS:

`python -m pip install --no-index --find-links=DIR -r requirements.txt`

Windows:

`py -m pip install --no-index --find-links=DIR -r requirements.txt`

# “Only if needed” Recursive Upgrade

`pip install --upgrade` now has a `--upgrade-strategy` option which controls how pip handles 
upgrading of dependencies. There are 2 upgrade strategies supported:

* `eager`: upgrades all dependencies regardless of whether they still satisfy the new parent 
  requirements
  
* `only-if-needed`: upgrades a dependency only if it does not satisfy the new parent requirements

The default strategy is `only-if-needed`. This was changed in pip 10.0 due to the breaking nature of 
`eager` when upgrading conflicting dependencies.

As an historic note, an earlier “fix” for getting the `only-if-needed` behaviour was:

Unix/macOS:

```
python -m pip install --upgrade --no-deps SomePackage
python -m pip install SomePackage
```

Windows:

```
py -m pip install --upgrade --no-deps SomePackage
py -m pip install SomePackage
```

A proposal for an `upgrade-all` command is being considered as a safer alternative to the behaviour of 
eager upgrading.

# User Installs

With Python 2.6 came the [“user scheme” for installation](https://docs.python.org/3/install/index.html#alternate-installation-the-user-scheme), which means that all Python distributions 
support an alternative install location that is specific to a user. The default location for each OS is 
explained in the python documentation for the [site.USER_BASE](https://docs.python.org/3/library/site.html#site.USER_BASE) variable. This mode of installation can 
be turned on by specifying the [--user](https://pip.pypa.io/en/stable/reference/pip_install/#install-user) option to `pip install`.

Moreover, the “user scheme” can be customized by setting the `PYTHONUSERBASE` environment variable, 
which updates the value of `site.USER_BASE`.

To install “SomePackage” into an environment with site.USER_BASE customized to ‘/myappenv’, do the 
following:

Unix/macOS:

```
export PYTHONUSERBASE=/myappenv
python -m pip install --user SomePackage
```

Windows:

```
set PYTHONUSERBASE=c:/myappenv
py -m pip install --user SomePackage
```

`pip install --user` follows four rules:

1. When globally installed packages are on the python path, and they _conflict_ with the installation 
   requirements, they are ignored, and _not_ uninstalled.
   
2. When globally installed packages are on the python path, and they _satisfy_ the installation 
   requirements, pip does nothing, and reports that requirement is satisfied (similar to how global 
   packages can satisfy requirements when installing packages in a `--system-site-packages `
   virtualenv).
   
3. pip will not perform a `--user` install in a `--no-site-packages` virtualenv (i.e. the default kind of 
   virtualenv), due to the user site not being on the python path. The installation would be pointless.
   
4. In a `--system-site-packages` virtualenv, pip will not install a package that conflicts with a package in 
   the virtualenv site-packages. The --user installation would lack sys.path precedence and be pointless.
   
To make the rules clearer, here are some examples:

From within a `--no-site-packages` virtualenv (i.e. the default kind):

Unix/macOS:

```
$ python -m pip install --user SomePackage
Can not perform a '--user' install. User site-packages are not visible in this virtualenv.
```

Windows:

```
C:\> py -m pip install --user SomePackage
Can not perform a '--user' install. User site-packages are not visible in this virtualenv.
```

From within a `--system-site-packages` virtualenv where `SomePackage==0.3` is already installed in the 
virtualenv:

Unix/macOS:

```
$ python -m pip install --user SomePackage==0.4
Will not install to the user site because it will lack sys.path precedence
```

Windows:

```
C:\> py -m pip install --user SomePackage==0.4
Will not install to the user site because it will lack sys.path precedence
```

From within a real python, where `SomePackage` is _not_ installed globally:

Unix/macOS:

```
$ python -m pip install --user SomePackage
[...]
Successfully installed SomePackage
```

Windows:

```
C:\> py -m pip install --user SomePackage
[...]
Successfully installed SomePackage
```

From within a real python, where `SomePackage` _is_ installed globally, but is _not_ the latest version:

Unix/macOS:

```
$ python -m pip install --user SomePackage
[...]
Requirement already satisfied (use --upgrade to upgrade)
$ python -m pip install --user --upgrade SomePackage
[...]
Requirement already up-to-date: SomePackage
# force the install
$ python -m pip install --user --ignore-installed SomePackage
[...]
Successfully installed SomePackage
```

Windows:

```
C:\> py -m pip install --user SomePackage
[...]
Requirement already satisfied (use --upgrade to upgrade)
C:\> py -m pip install --user --upgrade SomePackage
[...]
Requirement already up-to-date: SomePackage
# force the install
C:\> py -m pip install --user --ignore-installed SomePackage
[...]
Successfully installed SomePackage
```

From within a real python, where `SomePackage` _is_ installed globally, and is the latest version:

Unix/macOS:

```
$ python -m pip install --user SomePackage
[...]
Requirement already satisfied (use --upgrade to upgrade)
$ python -m pip install --user --upgrade SomePackage
[...]
Requirement already up-to-date: SomePackage
# force the install
$ python -m pip install --user --ignore-installed SomePackage
[...]
Successfully installed SomePackage
```

Windows:

```
C:\> py -m pip install --user SomePackage
[...]
Requirement already satisfied (use --upgrade to upgrade)
C:\> py -m pip install --user --upgrade SomePackage
[...]
Requirement already up-to-date: SomePackage
# force the install
C:\> py -m pip install --user --ignore-installed SomePackage
[...]
Successfully installed SomePackage
```

# Ensuring Repeatability

pip can achieve various levels of repeatability:

<h3>Pinned Version Numbers</h3>

Pinning the versions of your dependencies in the requirements file protects you from bugs or 
incompatibilities in newly released versions:

```
SomePackage == 1.2.3
DependencyOfSomePackage == 4.5.6
```

Using pip freeze to generate the requirements file will ensure that not only the top-level dependencies 
are included but their sub-dependencies as well, and so on. Perform the installation using --no-deps for 
an extra dose of insurance against installing anything not explicitly listed.

Full info you can see: [here](https://pip.pypa.io/en/stable/user_guide/#pinned-version-numbers)