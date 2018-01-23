import subprocess
from os import listdir, path
from app.base_settings import cron_logger

try:
    mod_path = path.dirname(path.realpath(__file__))

    def job():
        def update_repo():
            command = """git pull origin master"""
            git_response = subprocess.check_output([command], shell=True).decode('utf-8')
            if git_response.startswith('Already'):
                cron_logger.info('TestCron: No update in jobs')
            jobs = [mod_path + '/jobs/jobs_to_do/' + job_ for job_ in listdir(mod_path + '/jobs/jobs_to_do/')]
            for job in jobs:
                cron_logger.info(subprocess.check_output(['~/env/hippo/bin/python {}; '
                                                          'mv {} {}; git add .; '
                                                          'git commit -m "moved {} to done";'
                                                         .format(job, job, mod_path+'/jobs/jobs_done/', job)],
                                                         shell=True)
                                 .decode('utf-8'))

            else:
                cron_logger.info('TestCron: Change detected in jobs, running all under jobs/jobs_to_do')
                jobs = [mod_path + '/jobs/jobs_to_do/' + job_ for job_ in listdir(mod_path + '/jobs/jobs_to_do/')]
                for job in jobs:
                    cron_logger.info(subprocess.check_output(['~/env/hippo/bin/python {}'.format(job)], shell=True)
                                     .decode('utf-8'))

        update_repo()


    job()
except Exception as e:
    cron_logger.error(e)