import logging
import os
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get the setting named 'myAppSetting'
    my_app_setting_value = os.environ["myAppSetting"]
    logging.info(f'My app setting value:{my_app_setting_value}')

main()
