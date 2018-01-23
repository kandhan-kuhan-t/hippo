import schedule
import time
import subprocess
from os import listdir, path
from app.base_settings import cron_logger

mod_path = path.dirname(path.realpath(__file__))


def job():
    def update_repo():
        command = """git pull origin master"""
        git_response = subprocess.check_output([command], shell=True).decode('utf-8')
        if git_response.startswith('Already'):
            cron_logger.info('No update in jobs')
        else:
            cron_logger.info('Change detected in jobs, running all under jobs/jobs_to_do')
            jobs = [mod_path + '/jobs/jobs_to_do/' + job_ for job_ in listdir(mod_path + '/jobs/jobs_to_do/')]
            for job in jobs:
                cron_logger.info(subprocess.check_output(['~/env/hippo/bin/python {}'.format(job)], shell=True)
                                 .decode('utf-8'))
    update_repo()


schedule.every(5).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
