from flask import Flask, render_template
import broadlink
import binascii
import pprint
from time import sleep

from commands import commands
from scenes import scenes

device = broadlink.discover(timeout=5)[0]
device.auth()
devtype = device.get_type()
devnet = device.host[0]
devmac = binascii.hexlify(device.mac).decode('utf-8')
pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cmdlist")
def cmdlist():
    return render_template('cmdlist.html', cmdlist=pp.pformat(commands))

@app.route("/scenelist")
def scenelist():
    return render_template('scenelist.html', scenelist=pp.pformat(scenes))


@app.route("/devinfo")
def devinfo():
    return render_template('devinfo.html', type=devtype, net=devnet, mac=devmac)

@app.route("/sendcmd")
@app.route("/sendcmd/<cmd>")
def sendcmd(cmd=None):
    if cmd == None:
        return "No command given. Try /sendcmd/&lt;command&gt;"
    elif cmd.lower() in commands:
        device.send_data(commands[cmd.lower()])
        return "Sending "+cmd+" to "+devnet
    else:
        return "Command "+cmd+" is not an <a href='/cmdlist'>known</a> command."

@app.route("/loopcmd")
@app.route("/loopcmd/<cmd>/<cnt>")
def loopcmd(cmd=None,cnt=1):
    if cmd == None:
        return "No command given. Try /loopcmd/&lt;command&gt;/&lt;count&gt;"
    elif cmd.lower() in commands:
        for _ in range(int(cnt)):
            device.send_data(commands[cmd.lower()])
            sleep(0.2)
        return "Sending "+cmd+" "+cnt+" times to "+devnet
    else:
        return "Command "+cmd+" is not an <a href='/cmdlist'>known</a> command."



@app.route("/sendscene")
@app.route("/sendscene/<scene>")
def sendscene(scene=None):
    if scene == None:
        return "No scene given. Try /sendscene/&lt;scene&gt;"
    elif scene.lower() in scenes:
        for cmd in scenes[scene.lower()]:
            if cmd == None:
                return "No command given. Try /sendcmd/&lt;command&gt;"
            elif cmd.lower() in commands:
                device.send_data(commands[cmd.lower()])
            else:
                return "Command "+cmd+" is not an <a href='/cmdlist'>known</a> command."
            sleep(0.5)
        return "Executing scene "+scene+" via "+devnet
    else:
        return "Scene "+scene+" is not an <a href='/scenelist'>known</a> scene."
