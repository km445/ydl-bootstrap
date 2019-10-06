result_backend = 'redis://localhost'
result_expires = 60 * 15
broker_url = 'amqp://'
task_serializer = 'json'
result_serializer = 'json'
include = ['proj.tasks']
task_routes = {"proj.tasks.download_file_cpu_bound": "cpu_bound",
               "proj.tasks.download_file_io_bound": "io_bound"}
