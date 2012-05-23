# -*- coding: utf-8 -*-
# speech.py
import Skype4Py

VOICE='Kyoko'

def Say(message):
    import commands
    print message
    status , command = commands.getstatusoutput('/usr/bin/say -v %s "%s"' % (VOICE, message.encode('utf-8'),))

COMMANDS = {
    'say': Say
}

def Parse(body):
    msgs = body.split(' ')
    try:
        # parse
        cmd = msgs[0]
        message = u' '.join(msgs[1:]).replace('"', "'")

        # execute
        COMMANDS[cmd](message)

    except:
        pass


def OnMessageStatus(Message, Status):
    if Status == 'RECEIVED':
        print(Message.FromDisplayName + ': ' + Message.Body)
        Parse(Message.Body)

    if Status == 'READ':
        pass

    if Status == 'SENT':
        print(Message.FromDisplayName + ': ' + Message.Body)
        Parse(Message.Body)


def main():
    skype = Skype4Py.Skype()
    skype.Attach()
    skype.OnMessageStatus = OnMessageStatus

    Cmd = ''
    while not Cmd == 'exit':
        Cmd = raw_input('')

if __name__ == '__main__':
    main()
