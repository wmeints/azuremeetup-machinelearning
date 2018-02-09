# Environment setup instructions
For the challenges you will be using Azure Machine Learning Workbench.
Follow these instructions to create an Azure Machine Learning Experimentation 
environment and install the Azure Machine Learning Workbench.

## Step 1: Create an Azure Machine Learning Experimentation environment
Open up the azure portal and search for `machine learning`. A list of possible 
resources shows up, among them the `Azure Machine Learning Experimentation` 
resource.

![Create a new experiment](images/create-experiment.png)

Select the experimentation resource type and click the `Create` button.

**Quick link**: [Open the create experiment dialog](http://bit.ly/2ERn12j)

## Step 2: Specify the details for your experimentation environment
You'll now see a screen that allows you to specify the properties of your 
environment.

![Experiment details](images/experiment-details.png)

Specify the following properties:

 * The name of the experiment
 * A storage account for the experiment
 * The name of the experiment workspace
 * A model management account

 **Note** Please specify the dev/test pricing tier for the model 
 management account. This is a free option that will ultimately save you
 a lot of money.

Now click the create button and grab something to drink. It will take a few
minutes for the resources to be created. 

 ## Step 3: Download the tools
 Once you have confirmation that the deployment is done, navigate to the 
 experiment you just created. 

 ![The experiment quickstart page](images/experiment-quickstart.png)

 The page you'll see is a quickstart for the Azure Machine Learning experiment.
 It contains links to the tools that will help you build your experiment.

 Click the download link for the Azure Machine Learning Workbench tool for the
 platform of your choice. 

 **Note** As of the moment of writing only Mac and Windows are supported.

 ## Step 4: Install the tools
 After you downloaded the tool, start the installation and follow the 
 instructions to install the Azure Machine Learning Workbench on your machine.

 ## Step 5: Open the tool and create a new project
 Once installed, open the Azure Machine Learning Workbench. Login with your
 microsoft account and select the experiment that you've just created.

 ![Launch screen](images/ml-workbench-start.png)

 Now you're ready to get started with [Challenge 1](challenge-1/README.md).