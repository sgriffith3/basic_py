# Using Python to Send Email

### Lab Objective
The objective of this lab is to learn how to use the **pynapl** package to send emails. 

The **pynapl** package enables users to send mail using its built in `send_mail` function. This is useful for sending quick emails to a single individual (or for emailing yourself to make sure that you have your correct server settings enabled). Or, if you are attempting to automate sending a bunch of emails (like parsing through a csv file with dozens of name/email address combos to send "personalized" emails), pynapl is going to work well for you as well.

The **pynapl** package parameters:

|Parameter | Type| Description|
|---|---| ---|
|send_from | _str_ |Your email address`*`|
|send_to | _list of str(s)_| Their email address(es)`*`|
|password | _str_ | Your email password`*`|
|text | _str_ | The text/HTML string that you wish to send|
|subject| _str_ | The subject of your email|
|files| _list of str(s)_ | The files you wish to send from the local directory
|server| _str_ | The server you are sending the email from - default 'smtp.gmail.com'|
|port| _str_ | The secure port you are sending the email from |


You will have to set your password earlier in the script before using it, and pass your password as an argument within the function. 

### Procedure
0. Before you are going to be able to use the pynapl package, you are going to need to have it installed. Download it using pip from within your linux shell.

    `$` `pip3 install pynapl`
    
0. Once that has downloaded, go ahead and open up a new file called `send-email.py`

    `$` `vim send-email.py`
    
0. After your shebang line, you are going to need to first import the pynapl package before being able to call it in your code. Copy the following code into your file.

        #!/usr/bin/python3
        
        import pynapl
        import getpass
        
        passw = getpass.getpass("What is your email password? ")
        pynapl.send_mail("<your-email-goes-here>", ["<receiver(s)'s email goes here as a list>"],\
        password=passw, subject="Sending an email using pyapl", \
        text="Hello! This is my first time sending an email using pynapl.") 
        
    > Before going any further, make sure you place your email in where it says `<your-email-goes-here>`, and put in either your email address or another viable email address in the `<receiver(s)'s email goes here as a list>` section.
        
0. Run your script. You will be prompted for your email password. This will be sent to the server to authenicate your session and allow python to send the email.

    `$` `python3 send-email.py`
    
0. Verify that you have sent the email. Once you are sure that it is working, proceed on to the next step.

0. You next are going to need to create a csv file with the format of `<name>,<email address>` with as many email addresses as you wish. The following example just has two name/email combo, but it will work with as many as you can come up with.

    `$` `vim emails-to-send.csv`
    
        Sam,sgriffith@alta3.com
        <your name>,<your email address>
        
    > Add as many name/email combos as you wish. Just don't overuse this tool, or people might start blocking you.
    
0. Next, create the following python file, named `parsed-email.py`. **USE CAUTION**, this is going to send out your `emails-to-send.csv` file by default. If you do not wish for everybody on your list to receive this list, feel free to switch it for another file.

    `$` `vim parsed-email.py`
    
        #!/usr/bin/python3
        
        import pynapl
        import getpass
        
        passw = getpass.getpass("What is your email password? ")
        with open("emails-to-send.csv", "r") as ems:
            for row in ems:
                ems1 = row.split(",")
                name = ems1[0]
                recip = ems1[1]
                txt = "Hello {}, I am sending you an email with pynapl".format(name)
                subj = "Hey {}!".format(name)
                fil = ["send-email.py", "emails-to-send.csv"]
                pynapl.send_mail("<your-email-goes-here>", [recip], password=passw, subject=subj, text=txt)   
                
0. Run your script. It should prompt you for your password one time, then send out your email to every recipient in your csv file, inputting their name to make it feel more personalized.

***Congratulations! You now have the power to send emails using Python!***
