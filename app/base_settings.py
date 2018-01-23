import logging
import logging.handlers

FORMAT = '%(asctime)s, %(levelname)s : %(pathname)s,  %(message)s'

exceptions_fh = logging.handlers.RotatingFileHandler(".exceptions.log", maxBytes=204800)
exceptions_fh.setLevel(logging.ERROR)
exceptions_fh.setFormatter(logging.Formatter(FORMAT))

cron_logger = logging.getLogger('Cron')
fh = logging.handlers.RotatingFileHandler(".cron.log", maxBytes=20480)
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(FORMAT))
cron_logger.addHandler(fh)
cron_logger.addHandler(exceptions_fh)
cron_logger.setLevel(logging.DEBUG)
cron_logger.debug("testing log")

mail_logger = logging.getLogger('Mail')
mail_fh = logging.handlers.RotatingFileHandler(".mail.log", maxBytes=20480)
mail_fh.setLevel(logging.DEBUG)
mail_fh.setFormatter(logging.Formatter(FORMAT))
mail_logger.addHandler(mail_fh)
mail_logger.addHandler(exceptions_fh)
mail_logger.setLevel(logging.DEBUG)
mail_logger.debug("testing log")
mail_logger.error("Error testing")

