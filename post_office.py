from typing import List


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name, messages_number=1000000) -> List:
        """
        Returns a number of requested messages from the box and marks them as read.
        :param str user_name: Username from which the messages will be read.
        :param int messages_number: The number of messages to read.
        :return: List of messages read.
        :rtype list
        """
        messages = [self.boxes[user_name] for mes in self.boxes[user_name] if mes.message_id <= messages_number]
        self.boxes[user_name].pop(messages)
        return messages

    def search_inbox(self, user_name, message) -> List:
        """
        Returns all messages that contain a particular string.
        :param str user_name: Username from which the messages will be read.
        :param message: The same string should be searched for in messages.
        :return: The list of messages that contain the string.
        :rtype list
        """
        return [self.boxes[user_name] for mes in self.boxes[user_name] if message in mes]
