#!/usr/bin/env python3
# Code from Coursera

# To trigger the error, LANG=en_US, UTF-8

import datetime
import email
import smtplib
import sys

def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("    send_reminders 'date|Meeting|Emails' ")
    return 1

def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi all!
    
This is a quick mail to remind you all that we have a meeting about: "{title}""
the {weekday} {date}

See you there.
''')
    return message

def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names[row[0]] = row[1]
    return names

def send_message(message, emails):
    smtp = smtplib.SMTP('localhost')
    names = read_names(contacts)
    for email in emails.split(','):
        name = names[email]
        message = message_template(date, title, name)
        message['From'] = 'noreply@example.com'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, time, emails = sys.argv[1].split('|')
        message = message_template(date, time)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email with: {}".format(e), file=sys.stderr)

if __name__ == '__main__':
    sys.exit(main())