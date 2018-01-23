from typing import Tuple, List
from celery import Celery
from sparkpost import SparkPost


class Mailer:
    """
    This is an interface for creating a Mailer
    """
    def send_mail(self, from_address: str, to_addresses, subject: str, message: str,
                  test: bool=False, *args, **kwargs):
        raise NotImplementedError(
            "This method has to be implemented"
        )

    def _send_mail(self, from_address: str, to_addresses: Tuple, subject: str, message: str,
                  test: bool, *args, **kwargs):
        raise NotImplementedError(
            "This method has to be implemented"
        )


class SparkpostMailer(Mailer):
    def __init__(self, api_key, test=False):
        self.api_key = api_key
        self.sp = SparkPost(api_key=api_key)
        self.test = test

    def _send_mail(self, from_address: str, to_addresses: List, subject: str, message: str, sandbox: bool,
                   *args, **kwargs):
        response = self.sp.transmissions.send(
            use_sandbox=sandbox,
            recipients=to_addresses,
            html=message,
            from_email=from_address,
            subject=subject
        )
        return response

    def send_mail(self, from_address: str, to_addresses: Tuple, subject: str, message: str,
                  test: bool=False, *args, **kwargs):
        sandbox = True if self.test or test else False
        to_addresses_list = list(to_addresses)
        return self._send_mail(from_address, to_addresses_list, subject, message, sandbox)

    def test_mail(self):
        return self.send_mail(
            from_address='test.techteam@mail.cyces.co',
            to_addresses=('kandhan.kuhan@gmail.com', 'thecorptechteam@gmail.com'),
            subject='Testing',
            message='Testing'
        )


app = Celery('worker', broker='redis://localhost:6379/0')

# option for api_key to be read from .env file, use dotenv
mailer = SparkpostMailer(api_key='1e501df8906e2a6553ca434c3efaa49e3376baf4')


@app.task
# Create send_mail decorator with below key parameters accepting a mailers instance
def send_mail(from_address: str, to_addresses: Tuple, subject: str, message: str,
                  test: bool=False, *args, **kwargs):
    return mailer.send_mail(from_address, to_addresses, subject, message, test, *args, **kwargs)


# send_mail('support@mail.cyces.co', ('kandhan.kuhan@gmail.com', ), 'testing', 'testing')