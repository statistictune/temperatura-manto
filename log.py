import logging


class Log:
    def beggin_log(args):
        # Creating and Configuring Logger

        log_Format = "%(levelname)s %(asctime)s - %(message)s"

        logging.basicConfig(
            level=logging.INFO,
            format=log_Format,
            handlers=[logging.FileHandler("logfile.log"), logging.StreamHandler()],
        )

        logging.info(args)

        return logging
