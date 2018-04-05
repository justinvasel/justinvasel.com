# Justin Vasel's Official Website

![GitHub (pre-)release](https://img.shields.io/github/release/justinvasel/justinvasel.com/all.svg)
![Travis](https://img.shields.io/travis/justinvasel/justinvasel.com.svg)


## About

I'm Justin. I do physics and stuff. This is the codebase for my personal/professional website https://www.justinvasel.com.


## Technologies

* [Python 2.7](https://www.python.org/) (including pip)
* [Flask](http://flask.pocoo.org/)
* [Apache 2](https://httpd.apache.org/)
* [Let's Encrypt](https://letsencrypt.org/) (for SSL)
* [Digital Ocean](https://www.digitalocean.com/) (hosting)


## Usage

If you want to get this site up and running for yourself, feel free to clone
this repo and then do the following:

```shell
# If you already have virtualenv installed, skip this step
pip install virtualenv

# Do either A or B below to install required libraries

# A) Install the components automagically
make

# B) Do it manually if you want
virtualenv env
source env/bin/activate
pip install -r requirements.txt

# Spin up the development version of the application
python serve.py
```

Once that is up and running. Point your browser to `http://127.0.0.1:5002`.

**Note:** In future, you'll need to set up the local environment with
`source env/bin/activate` before spinning up the server.

This project follows common Flask practices. HTML files are in `app/templates`
and use Jinja templates. Static assets (like css, js, etc) are in `app/static`.


## Contributing

Pull requests are welcome, but will only be accepted on a case-by-case basis.
This is my personal website, after all.


## License

Feel free to fork this and make it your own. See [LICENCE.md](LICENSE.md) for
more details.
