from typing import Any, overload

class MailMessage_:

	#---Attributes---#
	REGS_VersionString: str

	REGI_Version: int

	REGB_Hide: bool

	REGB_SupportsDoD: bool

	REGI_ClassType: int

	REGI_Priority: int

	REGS_ID: str

	REGS_Name: str

	REGB_Unpredictable: bool

	REGB_ControlView: bool


	#---Methods---#
	@overload
	def AddRecipients(self, addresses: str) -> None:
		"""
		Adds a recipient to the To: list

		Arguments:
			 Addresses - a string of containing one or more email addresses,
									 or table of email address strings (or name/address string pairs)
		"""
		...
	@overload
	def AddRecipients(self, addresses: dict[Any, Any]) -> None:
		"""
		Adds a recipient to the To: list

		Arguments:
			 Addresses - a string of containing one or more email addresses,
									 or table of email address strings (or name/address string pairs)
		"""
		...
	def RemoveAllRecipients(self) -> None:
		"""
		Removes all recipients from the To: field
		"""
		...
	def SetPassword(self, password: str) -> None:
		"""
		Sets the password to use for authentication

		password - a string containing the plaintext password
								 to use when authenticating with the server.
		"""
		...
	def SetLogin(self, login: str) -> None:
		"""
		Sets the login to use for authentication

		Arguments:
			 login - a string containing the login or email address
								 to use when authenticating with the server.
		"""
		...
	def SetServer(self, servername: str) -> None:
		"""
		Sets the outgoing mail server to use

		Arguments:
			 servername - a string containing the domain name of the SMTP server
								 to use when sending mail.

		Note: If servername is empty (the default), the Prefs->Network field
					or direct MX lookup will be used.
		"""
		...
	@overload
	def SetSender(self, sender: str) -> None:
		"""
		Sets the From: field

		sender - a string with the sender's address (or name and address),
								 or a table containing strings of the sender's name
								 and email address.

		Note: If the sender is not set, it will default to the user's
					primary email name and address.
		"""
		...
	@overload
	def SetSender(self, sender: dict[Any, Any]) -> None:
		"""
		Sets the From: field

		sender - a string with the sender's address (or name and address),
								 or a table containing strings of the sender's name
								 and email address.

		Note: If the sender is not set, it will default to the user's
					primary email name and address.
		"""
		...
	def SetSubject(self, subject: str) -> None:
		"""
		Sets the Subject: field
		"""
		...
	def SetHTMLBody(self, bodyhtml: str) -> None:
		"""
		Sets the message body using HTML
		"""
		...
	def GetTable(self) -> dict[Any, Any]:
		"""
		Returns the message in the form of a table

		Usage: table = GetTable()

		Returns: table - a table with To, From, Subject and Body fields
										 containing the message data. Any attachment filenames
										 are listed in numbered fields.
		"""
		...
	def AddAttachment(self, filename: str) -> bool:
		"""
		Attaches a filename to the body
		"""
		...
	def RemoveAllAttachments(self) -> None:
		"""
		Removes all attachments from the message
		"""
		...
	def Send(self, timeout: int = int()) -> tuple[bool, str]:
		"""
		Sends the message

		Arguments: timeout - (optional) network timeout in milliseconds

		Returns: success - true if the message was sent OK
						 log		 - nil, or a string containing a log of error messages
		"""
		...
	def header_text(self) -> None:
		...
	def SetBody(self, bodytext: str) -> None:
		"""
		Sets the message body
		"""
		...

MailMessage = MailMessage_