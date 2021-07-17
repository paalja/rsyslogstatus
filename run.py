from flask import Flask, render_template, redirect, url_for, request, session, app
from list import *
from datetime import timedelta
import os
import time


app = Flask(__name__)



@app.route("/status", methods=['POST', 'GET'])
def shstatus():

    switchlist = 'hei liste'
    host = None
    dev = None


    if request.method == 'POST':

        unique_list = ['0']
        int_name = ['1']
        int_status = ['2']
        int_vlan = ['3']
        int_duplex = ['4']
        int_speed = ['5']
        int_type = ['6']
        int_lastinput = ['7']
        host = request.form['ik']
        #unique_list = list
        #int_port, int_name, int_status, int_vlan, int_duplex, int_speed, int_type, int_lastinput = list
        #col = zip(int_port, int_name, int_status, int_vlan, int_duplex, int_speed, int_type, int_lastinput)
        col = zip(unique_list, int_name, int_status, int_vlan, int_duplex, int_speed, int_type, int_lastinput)

    elif request.form.get('DB1') == 1:
        asdf = request.form.getlist('DB1')

    else:
        switches = switchlist
        return render_template('status.html', day=timeanddate(), host=host, dev=dev)  # first page
        print('else')

    switches = switchlist()
    return render_template('status.html', day=timeanddate(), host=host, col=col)  # first page after

@app.route('/day')
def timeanddate():
    day = time.strftime('%A %d %B %Y %H:%M:%S')
    return day

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)