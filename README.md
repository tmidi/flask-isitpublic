# flask-isitpublic

## Build Status:
[![Build Status](https://travis-ci.org/tmidi/flask-isitpublic.svg?branch=master)](https://travis-ci.org/tmidi/flask-isitpublic)

## Description:
isitpublic is simple Flask application to check if an IP adress is Public or Private and provide basic explanation for what's a public or a private address is.

## Install:
### Build:
You can clone this repository to manually build the container image:

```bash
# Clone Repo:
git clone git@github.com:tmidi/flask-isitpublic.git

# Build Docker image:
docker build -t flask-isitpublic --file Dockerfile

# Run image:
docker run -p 5000:5000 flask-isitpublic

```
### Use public image:
```bash
# Pull image:
docker pull taleeb/isitpublic

# Run container 
docker run -p 5000:5000 taleeb/isitpublic 
```

## License

This repo is available under [MIT](https://github.com/eucalyptuss/ikonate/blob/master/LICENSE). Feel free to use the set in both personal and commercial projects. Attribution is much appreciated but not required.
