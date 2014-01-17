# coalio

Application for HackDance 2014

## Contributing

### Clone the repo

1. `git clone git@github.com:octaflop/coalio.git`
2. `cd coalio`

### Install [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and set up

1. Install pip
2. Install `virtualenvwrapper`
  * `pip install virtualenvwrapper`
  * `source /usr/local/bin/virtualenvwrapper.sh`
  * You will want to add this line to your `.bashrc` or `.bash_profile`
3. Add the apps directory to the virtualenv: 
```bash
    add2virtualenv `pwd`apps 
```
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

## Pushing to production

1. Email your ssh public key to faris ☺
2. Add the remote repo: `git remote add production git@198.58.106.50:coalio.git`
3. Now you can push `master` branches to the production server by using: `git push production master`! (Be sure to push to origin so we're all on the same page: `git push origin master`).

