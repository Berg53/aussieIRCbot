import os
import random
count = 0
def find_quote(username=None, text=None):
    with open('/home/berg/bin/aussieIRCbot/src/aussie_bot/data/quote.txt') as quote_file:
        
        try:

            message = random.choice([x for x in quote_file.readlines() if text in x])
            return message



            
        except Exception as e:
            print(e)
            return "{} The only thing I can find is your arrest warrant..God wills it!!!!".format(username)
  
    
        
 






def newest():
    try:
        path = '/home/berg/bin/aussieIRCbot/src/aussie_bot/logs/freenode/channels'
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        return (max(paths, key=os.path.getctime))
    except:
        return



def save_quote(username, text):
    try:
        count = 0
        lines = {}
        print(text)
        quotes_file = newest()
        print(quotes_file)
        for line in open(quotes_file,'r'):
            if text in line:
                lines[count] = line
                count += 1 
                #tx is spamming me nodebot@103.1.54.130 PRIVMSG ###aussies :!save hAng
                print(username)
                if username.find('bot') != -1:
                    return"Well Well Well!"

               
                if "!save" in line or "Meaty_Bot" in line or "!quot" in line or "Added Quote" in line or "|<--" in line or "Igor_Bot" in line:
                    count = count-1
        print(lines)
        num = count-1
        message = (lines[num])
        print(lines)
        quotes_file = ('/home/berg/bin/aussieIRCbot/src/aussie_bot/data/quote.txt')
        print('Begbug {}'.format(lines[num]))
        with open(quotes_file, 'a') as f:
            f.write(message)
            f.close()
        return "Yeth MATHTA {}: {}".format(username, message)
    except Exception as e:
        print(e)
        return "well thats not in the logs Master {}".format(username)



def handler(connection, event):
    username = event.source.nick
    users = event.source.nick
    print("debugs  ================={} ".format(users))
    print(event.arguments)
    try:
        command, text = event.arguments[0].split()
        print(event.target)
    except:
        return
    
    try:
        if event.arguments and command == "!save":
            message = save_quote(username, text)
            connection.privmsg(event.target, message.strip())
        if event.arguments and command == "!quote":
            message = find_quote(username, text)
            connection.privmsg(event.target, message.strip())
            

    except:
        return"no way it dont work"


def get_handlers():
    return (("pubmsg", handler),)

