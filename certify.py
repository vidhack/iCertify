import sys

from lib.config import config
from lib.editor import write_text_to_image, logit, get_statistics
from lib.communicate import send_email


def main():
    try:
        if sys.argv[1] == '--admin':
            print 'loading statistics...'
            get_statistics()
            return
        parameters = {'name': " ".join(sys.argv[2:]),
                      'email': sys.argv[1]
                      }
    except IndexError:
        print "USAGE : python certify <email_id> <full_name_with_space>"
        print "ADMIN USAGE : python certify --admin"
        return
    print "\nPlease wait, sending mail to %(email)s for %(name)s certificate..." % (parameters)
    heading = config.get('email-sender', 'subject')
    attachments = [write_text_to_image(parameters['name'])]
    send_email(parameters.get('email'), heading, open('data/emailer.html').read(), attachments, parameters)
    parameters['attachment'] = attachments[0]
    logit(parameters)

if __name__ == '__main__':
    main()
