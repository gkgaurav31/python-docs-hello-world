# Gunicorn configuration file
# https://docs.gunicorn.org/en/stable/configure.html#configuration-file
# https://docs.gunicorn.org/en/stable/settings.html
import gunicorn


max_requests = 1000
max_requests_jitter = 50

log_file = "-"

if gunicorn.version_info != (20, 0, 4):  # pragma: no cover
        raise ValueError(
                        "This monkey patch will probably need removing on later versions due"
                                + " to release of https://github.com/benoitc/gunicorn/pull/2233"
                                    )
        gunicorn.SERVER_SOFTWARE = "myserver"
