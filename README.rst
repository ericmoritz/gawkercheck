This is a really simple script to that takes a list of emails from stdin
and checks that email against the emails exposed Gawker's security breach.

Because Gawker didn't used irreversable hashes in their database, every user's
password could be decrypted very easily.

Test your own email::

    echo "test@example.com" | ./locate.py

Test against your gmail contacts (Exported using the "Google CSV" format)::

     cat google.csv | ./extract_gmail_addresses.py | ./locate.py

Now email your friends to let them know they're up shit's creek.
