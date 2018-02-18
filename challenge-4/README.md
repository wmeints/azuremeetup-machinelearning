# Challenge 4: Deploy your model to Azure
The first three challenges helped you build a model from the dataset. In this 
challenge we're going to build some components to use the model and then deploy
it to a production cluster.

## Preparation
Azure ML workbench exposes models as services through the use of `score.py`.
This file has a specific structure that you need to adhere to.

To help you get started, I went ahead and made the structure for you.

In the [starters](starters/) folder you'll find a `score.py` file. Copy
this to the root of your project.

## Step 1: Build the service for your model
In order to use a model in production we need to write some code to host the 
model. The input from the people that use your model should be validated and
converted into something that you can use in combination with your model.

Also, when you do a prediction, you want to convert it into a format that is
understood by the users of your model.

### Objective: Load the model from disk
Take a look at the `init` method. It currently shows a TODO comment for loading
the model. Azure ML will use the `init` function to intialize the service.

Typically you initialize global variables used in your service in this function.
Python has a need trick for this, any global variable assigned in a function
needs to be mentioned  in a `global`, preferrably at the start of the function.

For example, take a look at the code below:

```
global_var = None

def init():
    global global_var

    global_var = 42
```

This code first defines the `global_var` variable at the start of the script.
Then we define the `init` function and mention that `global_var` is a global
variable in the script. Then we assign the value.

Now when you use the `global_var` variable after you executed `init` it will have
the value 42. Without the global statement there would be a second `global_var`
in the function that has a different value than the globally defined one.

In the `init` method we need to load the model to the global model variable.
Complete this method by using the `pickle.load` method to load
the model from disk.

A sample of how to use the `load` method from the `pickle` module is shown below.

```
with open('some_file.pkl', 'rb') as input_file:
    model = pickle.load(input_file)
```

### Objective: Predict the price of a house
With the init method completed, let's move on to the `run` method. This method
is used for making predictions with your model.

In our case, we need to take the input from the user, put it through our model
and obtain a prediction.

Modify the run method so it accepts values for the features that you used in
building your model. For example, if you had the following features:

 * sqft_basement
 * sqft_above
 * bedrooms

You need the `run` function to look like this:

```
def run(sqft_basement, sqft_above, bedrooms):
   ....
```

Next make a prediction with your model. For this you need to invoke the 
`predict` method on your model. In my case it looks like this:

```
result = model.predict()
```

//TODO: Finish the excersise

### Objective: Publish the schema
//TODO: Explain how to generate the schema

## Step 2: Publish the service on Azure
//TODO: explain the second step