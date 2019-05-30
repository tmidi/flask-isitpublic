from flask import render_template, request
from forms import IpForm
from functions import is_valid_ipv4_address, is_valid_ipv6_address, netmask
from app import app


@app.route('/', methods=['POST', 'GET'])
def index():
    form = IpForm()
    if request.method == "POST" and form.validate():
        form = IpForm()
        ip = form.address.data

        if '/' in ip:
            return render_template("index.html",
                                   form=form,
                                   result=netmask(ip),
                                   ip=ip)

        elif ':' in ip:
            return render_template('index.html', form=form,
                                   result=is_valid_ipv6_address(ip),
                                   ip=ip)
        else:
            return render_template('index.html', form=form,
                                   result=is_valid_ipv4_address(ip),
                                   ip=ip)

    else:
        return render_template("index.html", form=form)
