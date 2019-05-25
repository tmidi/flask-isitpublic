from flask import render_template, request
import socket
import requests
from forms import IpForm
import ipaddress
from functions import is_valid_ipv4_address, is_valid_ipv6_address



from app import app


@app.route('/', methods=['POST', 'GET'])
def index():
    form = IpForm()
    error = ''
    result= ''
    if request.method == "POST" and form.validate():
        form = IpForm()
        ip = form.address.data
        if is_valid_ipv4_address(ip) or is_valid_ipv6_address(ip):
            if ipaddress.ip_address(ip).is_global:
                return render_template("index.html", form=form, result=True,error=error, ip=ip)
            else:
                return render_template("index.html", form=form, result=False,error=error, ip=ip)
        else:
            error = "Not a valid IP Address"
            return render_template("index.html", form=form, result=result, error=error)

    else:
        return render_template("index.html", form=form)
