import re
import sys
import pandas as pd

def parse_file(text_file):
    '''Convert WhatsApp chat log text file to a Pandas dataframe.'''
    
    # some regex to account for messages taking up multiple lines
    pat = re.compile(r'^(\d\d\/\d\d\/\d\d\d\d.*?)(?=^^\d\d\/\d\d\/\d\d\d\d|\Z)', re.S | re.M)
    with open(text_file) as f:
        data = [m.group(1).strip().replace('\n', ' ') for m in pat.finditer(f.read())]

    sender = []; message = []; datetime = []; keyword = []
    for row in data:

        # timestamp is before the first dash
        datetime.append(row.split(' - ')[0])

        # sender is between dash and colon
        try:
            s = re.search('- (.*?):', row).group(1)
            sender.append(s)
        except:
            sender.append('')

        # message content is after the first colon
        try:
            message.append(row.split(': ', 1)[1])
        except:
            message.append('')
	# keyword is in between * * (bold in whatsapp)
        try:
            st = re.findall(r'\*([^*]+)\*', row)
            keyword.append(st)
        except:
            keyword.append('')
        df = pd.DataFrame(list(zip(datetime, sender, keyword, message)), columns=['datetime', 'sender', 'keyword', 'message'])
        df.to_csv('whatsapp.csv')

df = parse_file('WhatsAppChatwithCIMBStocksSharing.txt')

