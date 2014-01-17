# coalio

Application for HackDance 2014

## Contributing

### Clone the repo

1. `git clone git@github.com:octaflop/coalio.git`
2. `cd coalio`

### Install Virtualenvwrapper and set up

1. Install pip
2. Install `virtualenvwrapper`
  * `pip install virtualenvwrapper`
  * `source /usr/local/bin/virtualenvwrapper.sh`
  * You will want to add this line to your `.bashrc` or `.bash_profile`
3. Add the apps directory to the virtualenv: `add2virtualenv \`pwd\`/apps` 
4. Configure the virtualenv (you will need to know your virtualenv directory):
eg: `vim ~/.virtualenvs/coalio/bin/postactivate`
5. Update the `DJANGO_SETTINGS_MODULE` setting to include this line:
`export DJANGO_SETTINGS_MODULE='coalio.settings.local'`
6. Reboot your virtualenv: `deactivate && workon coalio`

### Install dependencies

1. `cd` to your repo and install dependencies: `pip install -r requirements/base.txt`

### Let ‘er rip!

1. In the repo, run `./manage.py runserver`
2. Open `localhost:8000` in a browser.
