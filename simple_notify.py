import weechat
import subprocess

from libqtile.command import Client

c = Client()

USERNAME = "aero"

def currentbuffer():
    buf = weechat.current_buffer()
    return "#"+weechat.buffer_get_string(buf, "short_name")

weechat.register(
    "qtile_notify", "AeroNotix", "0.1", "GPL3", "Relay Privmessages to QTile", "", ""
    )

def catchpriv(data, signal, signal_data):
    
    m = weechat.info_get_hashtable(
        "irc_message_parse",
        {"message": signal_data},
        )

    if m['channel'] != currentbuffer() and USERNAME in m['arguments']:
        subprocess.call(
            ["mpg123","/home/aero/.weechat/python/autoload/notice.mp3"],
            stderr=open("/dev/null", "w"),
            stdin=open("/dev/null", "w")
            )
    if USERNAME in m['arguments']:
        c.widget["notice"].update(m['channel'])
    return weechat.WEECHAT_RC_OK

weechat.hook_signal("*,irc_in_PRIVMSG", "catchpriv", "")
