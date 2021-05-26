# i kinda threw this together in an hour lol

import random
import smtplib

GMAIL_CREDENTIALS = ('GMAIL_USERNAME@gmail.com', 'GMAIL_PASSWORD')

CARRIERS = {
    'att':    'mms.att.net',
    'tmobile':' tmomail.net',
    'verizon':  'vtext.com',
    'sprint':   'page.nextel.com'
}

if __name__ == '__main__':
    # get recipient data:
    recipients = {r.split()[0] : r.split()[1] for r in open('recipients.txt').readlines()}

    # choose a quote:
    quote = random.choice(open('quotes.txt').readlines())

    # and a nice message <3
    message = 'have a wonderful day! remember to smile a bit extra today <3 -ori'

    # get authentication details:
    gmail_username, gmail_password = GMAIL_CREDENTIALS

    # connect to gmail:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_username, gmail_password)

    # send the texts!
    for phone_number, carrier in recipients.items():
        try:
            phone_number = '%s@%s' % (phone_number, CARRIERS[carrier])
            server.sendmail(gmail_username, phone_number, quote)
            server.sendmail(gmail_username, phone_number, message)
        except Exception as e:
            print(e)
