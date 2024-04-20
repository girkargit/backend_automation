import json, requests
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
from timeit import default_timer as timer


class BackendAutomation():
    report_dataset = []

    user_token = ""
    user_dataset = {
        "application_id": "",
        "user_id": "",
        "offer_accp_id": "",
        "offer_prop_id": ""
    }
    required_dataset = {
        "automation_service": "",
        "file_path": "",
        "sub_sheet": "",
        "token": "",
        "report_file_name": ""
    }

    def __init__(self):
        print("Starting the application...")

        # self.codeForDebug()

        service_dataset = self.getTheRequiredInput()

        if not service_dataset['success']:
            print(service_dataset['message'])
            return

        ### process the file
        self.readTheExcelFile()

        ### generate the report
        self.generateReportFile()

    ### get the required data
    def getTheRequiredInput(self):
        service_dataset = {"success": True, "message": ""}
        for a_input in self.required_dataset:

            ### token not required
            if a_input == "token":
                continue

            ### get user input
            key_name = self.processInputKeyName(a_input)
            input_value = input(f"{key_name} :")
            input_value = input_value.replace("\"", "'")

            ### handle the condition
            if not input_value:
                service_dataset['success'] = False
                service_dataset['message'] = f"input {key_name} cannot be blank"
                return service_dataset

            self.required_dataset[a_input] = input_value

        return service_dataset

    ### process input key name
    def processInputKeyName(self, a_key):
        key_name = a_key.replace("_", " ")
        key_name = key_name.capitalize()

        return key_name

    ### read the excel file
    def readTheExcelFile(self):
        df = pd.read_excel(self.required_dataset['file_path'], engine="openpyxl",
                           sheet_name=self.required_dataset['sub_sheet'])
        df = df.replace({np.nan: None})

        for index, value in df.iterrows():

            ### process file data
            status_code, response_data = self.processFileData(value)

            if not status_code == 200:
                break

    ### process file data
    def processFileData(self, dataset):
        print(dataset)

        start_time = timer()

        ### construct the header
        if self.user_token:
            headers = {"Authorization": f"Token {self.user_token}"}
        else:
            headers = {}

        ### update the param and id
        dataset['API'] = dataset['API'].replace("--application_id", self.user_dataset['application_id'])
        dataset['API'] = dataset['API'].replace("--user_id", self.user_dataset['user_id'])
        dataset['API'] = dataset['API'].replace("--offer_prop_id", self.user_dataset['offer_prop_id'])

        dataset['Request Data'] = dataset['Request Data'].replace("--application_id",
                                                                  self.user_dataset['application_id'])
        dataset['Request Data'] = dataset['Request Data'].replace("--user_id", self.user_dataset['user_id'])
        dataset['Request Data'] = dataset['Request Data'].replace("--offer_prop_id", self.user_dataset['offer_prop_id'])

        ### handle the request
        if dataset['Method'] == "POST" or dataset['Method'] == "PUT":
            payload = json.loads(dataset['Request Data'])

            files = self.generateFileDataset(dataset)
            print(files)
            if not files:
                response = requests.request(dataset['Method'], dataset['API'], json=payload, headers=headers)
            else:
                response = requests.request(dataset['Method'], dataset['API'], data=payload, headers=headers,
                                            files=files)
        else:
            payload = json.loads(dataset['Request Data'])
            response = requests.get(dataset['API'], params=payload, headers=headers)

        ### end time
        end_time = timer()
        api_duration = "Duration - {}".format(timedelta(seconds=end_time - start_time))

        ### update the report
        dataset['Report Token'] = headers
        dataset['Status code'] = response.status_code
        dataset['Response Data'] = response.text
        dataset['API Duration'] = api_duration

        self.report_dataset.append(dataset)

        ### fetch token
        if "/super-app/validate-otp" in dataset['API'] and response.status_code == 200:
            response_data = response.json()
            self.user_token = response_data['data']['token']
            self.user_dataset['user_id'] = str(response_data['data']['user_id'])

        ### fetch application
        if "create-loan-application" in dataset['API'] and response.status_code == 200:
            response_data = response.json()
            self.user_dataset['application_id'] = str(response_data['data']['application_id'])

        ### fetch offer propose id
        if "/v1/fetch-proposed-offer" in dataset['API'] and response.status_code == 200:
            response_data = response.json()
            if "offer_data" in response_data['data']:
                self.user_dataset['offer_prop_id'] = str(response_data['data']['offer_data'][0]['id'])

        ### fetch offer accepted id
        if "call-api?source=LMS&datapoint=get_accepted_offers&endpoint" in dataset[
            'API'] and response.status_code == 200:
            response_data = response.json()
            self.user_dataset['offer_accp_id'] = str(response_data['data'][0]['id'])

        ### return the response
        return response.status_code, response.text

    ### generate report file
    def generateReportFile(self):
        df = pd.DataFrame(self.report_dataset)
        df.to_excel(self.required_dataset['report_file_name'], index=False)

    ### generate File dataset
    def generateFileDataset(self, dataset):

        if not dataset['File Path']:
            return None
        # try:
        # Remove extra double quotes around file paths
        excel_cell_value = dataset['File Path'].replace('""', '"')
        file_dataset = json.loads(excel_cell_value)
        files = {}

        for a_data in file_dataset:
            # with open(a_data['file_path'], 'rb') as file:
            # 	files[a_data['key_name']] = (a_data['file_path'], file)
            files[a_data['key_name']] = open(a_data['file_path'], 'rb')

        return files

    # except Exception as e:
    # 	return None

    ### verification code
    def codeForDebug(self):
        dataset = {}
        dataset[
            'File Path'] = '[{"file_path": "C:/Users/shubh/Downloads/front_aadhar.jpg", "key_name": "file_front"}, {"file_path":"C:/Users/shubh/Downloads/back_aadhar.jpg","key_name":"file_back"}]'
        # json_data = json.loads(dataset)

        files = self.generateFileDataset(dataset)
        print(files)


### call the main class
BackendAutomation()
