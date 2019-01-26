COMMAND_NOT_FOUND = "**** Command Not Found *****"
VALID_COMMANDS_ARE = "Valid Commands are"

CATEGORY_FIELD_NAME = "tags"

VALID = "Valid"
NOT_VALID = "Not Valid"
FOUND = "Found"
NOT_FOUND = "Not Found"
PRESENT = "Present"
NOT_PRESENT = "Not Present"
EXISTS = "Exists"
NOT_EXISTS = "Not Exists"

CORRECT_VPC_MSG = "Please update with correct VPC/CIDR/Subnet details in common.py OR create local.py and add VPC details"

PIP_CHECK_STARTED = "Checking Required Python Packages are Available"
PIP_CHECK_COMPLETED = "Required python packages are available!!!"

pip_required = "Please install all the required python packages to start the execution\n"
PIP_INSTALL_MSG = pip_required + "Please use ``` sudo pip3 install -r requirements.txt ``` from the installer directory\n\n"

TOOLS_CHECK_STARTED = "Checking Required Tools are available"
TOOLS_CHECK_COMPLETED = "Required Tools are available!!!"

INPUT_READING_STARTED = "Reading required inputs from user"
INPUT_READING_COMPLETED = "Required inputs are available!!!"

INVALID_KEY = "Entered Invalid Key!!!"
SETTINGS_CHECK_STARTED = "Checking settings and inputs"
VPC_CHECK_STARTED = "Checking VPC and CIDR Blocks"
SUBNETS_CHECK_STARTED = "Checking VPC Subnets"

INVALID_VPC = "VPC provided is not valid"
INVALID_CIDR = "Provided invalid CIDR Blocks lists"
INVALID_SUBNETS = "Invalid Subnets provided, please check"
INVALID_SUBNET_ZONES = "Subnets provided should be on different Availability Zones"

CHECKING_GROUP_POLICY = "Checking Group-Attached Policies"
CHECKING_USER_POLICY = "Checking User-Attached Policies"
FULL_ACCESS_POLICY = "Administrator Access Policy"
POLICY_YES_NO = "If you have added custom policies with all permissions, please type Yes or No"

LOG_DIR_NOT_FOUND = "Log DIrectory is not found"
LOG_DIR_SETTINGS_NOT_FOUND = "LOG_DIR path settings is required for the installation"

DATA_DIR_NOT_FOUND = "Log DIrectory is not found"
DATA_DIR_SETTINGS_NOT_FOUND = "DATA_DIR path settings is required for the installation"

RESOURCE_EXISTS_CHECK_STARTED = "Checking Resource Existence"
RESOURCE_EXISTS_CHECK_FAILED = "Resource existence check Failed \nPlease Delete all the existing resources or change their names\n"
RESOURCE_EXISTS_CHECK_COMPLETED = "Resource existence check Completed!!!"

TERRAFORM_GEN_STARTED = "Terraform file generation started"
TERRAFORM_GEN_COMPLETED = "Terraform file generation Completed!!!"

PROVIDER_NOT_FOUND = "Please add correct provider in configuration"
PROVISIONER_FILES_DIR_NOT_FOUND = "Provisioners files Directory is not found"
PROVISIONER_FILES_DIR_SETTINGS_NOT_FOUND = "Provisioners files Directory setting is not found"

TERRAFORM_INIT_STARTED = "Terraform Init started"
TERRAFORM_INIT_RUNNING = "Running Terraform init"
TERRAFORM_INIT_ERROR = "Terraform Init Encountered an error. Please check Error Log for more details"
TERRAFORM_INIT_COMPLETED = "Terraform Init executed successfully!!!"

TERRAFORM_PLAN_STARTED = "Terraform Plan started"
TERRAFORM_PLAN_RUNNING = "Running Terraform plan"
TERRAFORM_PLAN_ERROR = "Terraform Plan Encountered an error. Please check Error Log for more details"
TERRAFORM_PLAN_COMPLETED = "Terraform Plan executed successfully!!!"

TERRAFORM_APPLY_STARTED = "Terraform Apply started"
TERRAFORM_APPLY_RUNNING = "Creating / Updating resources"
TERRAFORM_APPLY_ERROR = "Terraform Apply Encountered an error. Please check Error Log for more details"
TERRAFORM_APPLY_COMPLETED = "Terraform Apply executed successfully!!! Please check Installation Log for more details"
TERRAFORM_APPLY_DRY_RUN = "Terraform Apply is not executed as DRY RUN is enabled"
TERRAFORM_OUTPUT_STORED = "Terraform Output is stored"

TERRAFORM_DESTROY_STARTED = "Terraform Destroy started"
TERRAFORM_DESTROY_RUNNING = "Destroying resources"
TERRAFORM_DESTROY_ERROR = "Terraform Destroy Encountered an error. Please check Error Log for more details"
TERRAFORM_DESTROY_COMPLETED = "Terraform Destroy executed successfully!!! Please check Destroy Log for more details"
TERRAFORM_DESTROY_DRY_RUN = "Terraform Destroy is not executed as DRY RUN is enabled"

TERRAFORM_TAINT_STARTED = "Terraform Taint(Destroy-ReInstall) started"
TERRAFORM_TAINT_ERROR = "Terraform Taint(Destroy-ReInstall) Encountered an error. Please check Error Log for more details"
TERRAFORM_TAINT_COMPLETED = "Terraform Taint(Destroy-ReInstall) executed successfully!!! Please check Installation log for more details"

EXECUTED_WITH_ERROR = "Execution encountered error"

RESOURCES_EMPTY = "There is nothing to process!"

APPLY_STATUS_COMPLETED = 'APPLY_STATUS_COMPLETED'
APPLY_STATUS_ERROR = 'APPLY_STATUS_ERROR'
DESTROY_STATUS_COMPLETED = 'DESTROY_STATUS_COMPLETED'
DESTROY_STATUS_ERROR = 'DESTROY_STATUS_ERROR'

STATUS_CODE_MSGS = {
    'APPLY_STATUS_COMPLETED' : "All resources are Created/Uodated successfully!",
    'APPLY_STATUS_ERROR' : "All resources are NOT Created/Uodated successfully. Apply encountered Error(s)",
    'DESTROY_STATUS_COMPLETED': "All resources are Destroyed successfully!",
    'DESTROY_STATUS_ERROR': "All resources are NOT Destroyed successfully. Destroy encountered Error(s)"
}

CURRENT_STATUS_MSG = "Current Status:"
NO_STATUS_OUTPUT = "Nothing to show as you have not Installed/Destroyed anything.\n"
CURRENTLY_INSTALLED_RESOURCES = "Currently Installed resources are:"

ALL_TOOLS_NOT_AVAIALABLE = "Please install all the required tools to start the execution\n"

ANOTHER_PROCESS_RUNNING = "Another process is running(Terraform Lock is Found). Please wait till it completes"
