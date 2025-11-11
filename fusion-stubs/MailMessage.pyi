from typing import Any, overload

class MailMessage:

    #---Registry---#
    REGI_ClassType: int

    REGB_ControlView: bool

    REGB_Hide: bool

    REGS_ID: str

    REGS_Name: str

    REGI_Priority: int

    REGB_SupportsDoD: bool

    REGB_Unpredictable: bool

    REGI_Version: int

    REGS_VersionString: str


    #---Methods---#
    def AddAttachment(self, filename: str) -> bool:
        """
        Attaches a filename to the body

        Args:
            filename (str)

        Returns:
            success (bool)
        """
        ...

    @overload
    def AddRecipients(self, addresses: str) -> None:
        """
        Adds a recipient to the To: list

        Arguments:
        Addresses - a string of containing one or more email addresses,
        or table of email address strings (or name/address string pairs)

        Args:
            addresses (str)
        """
        ...

    @overload
    def AddRecipients(self, addresses: list[str]) -> None:
        """
        Adds a recipient to the To: list

        Arguments:
        Addresses - a string of containing one or more email addresses,
        or table of email address strings (or name/address string pairs)

        Args:
            addresses (list[str])
        """
        ...

    def GetTable(self) -> dict[Any, Any]:
        """
        Returns the message in the form of a table

        Usage: table = GetTable()

        Returns: table - a table with To, From, Subject and Body fields
        containing the message data. Any attachment filenames
        are listed in numbered fields.

        Returns:
            msg (dict[Any, Any])
        """
        ...

    def RemoveAllAttachments(self) -> None:
        """
        Removes all attachments from the message
        """
        ...

    def RemoveAllRecipients(self) -> None:
        """
        Removes all recipients from the To: field
        """
        ...

    def Send(self, timeout: int | None = None) -> bool | str:
        """
        Sends the message

        Arguments: timeout - (optional) network timeout in milliseconds

        Returns: success - true if the message was sent OK
        log     - nil, or a string containing a log of error messages

        Args:
            timeout (Optional[int])

        Returns:
            success (bool)
            errlog (str)
        """
        ...

    def SetBody(self, bodytext: str) -> None:
        """
        Sets the message body

        Args:
            bodytext (str)
        """
        ...

    def SetHTMLBody(self, bodyhtml: str) -> None:
        """
        Sets the message body using HTML

        Args:
            bodyhtml (str)
        """
        ...

    def SetLogin(self, login: str) -> None:
        """
        Sets the login to use for authentication

        Arguments:
        login - a string containing the login or email address
        to use when authenticating with the server.

        Args:
            login (str)
        """
        ...

    def SetPassword(self, password: str) -> None:
        """
        Sets the password to use for authentication

        password - a string containing the plaintext password
        to use when authenticating with the server.

        Args:
            password (str)
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

        Args:
            sender (str)
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

        Args:
            sender (dict[Any, Any])
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

        Args:
            servername (str)
        """
        ...

    def SetSubject(self, subject: str) -> None:
        """
        Sets the Subject: field

        Args:
            subject (str)
        """
        ...

