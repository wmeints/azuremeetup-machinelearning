# Bring your AI experiment to production - Hands-on lab
This repository contains the challenges and data for the hands-on lab held at 
the dutch azure meetup. The goal of the workshop is to build a model to predict 
house prices and deploy the model to Azure.

This lab includes [slides](Bring%20your%20AI%20experiment%20to%20production.pptx) 
with an introduction.

## Prerequisites
To complete the challenges in this repository you need to have the following:

 * A Windows or Mac computer
 * An active Azure subscription

## Quickstart
Before you start working on the challenge you need to install some software on 
your computer. Please follow the instructions on 
[how to setup your environment](environment-setup.md).

After you're done with the setup, start with 
[the first challenge](challenge-1/README.md).

## Challenges
1. [Load and prepare the data](challenge-1/README.md)
2. [Explore the data using python notebooks](challenge-2/README.md)
3. [Build a model with Python and scikit-learn](challenge-3/README.md)
4. [Deploy your model to Azure](challenge-4/README.md)

## Copyright and other notifications
The data for this workshop comes from [harlfoxem](https://www.kaggle.com/harlfoxem) who hosted all 
[the house sales data](https://www.kaggle.com/harlfoxem/housesalesprediction) 
on Kaggle.com.

This data isn't meant for commercial use. This means that while you can use the 
workshop format in any way you like, I kindly remind you to get other data
if you plan to sell this workshop format for money.

## Changelog
**2018-04-09**
* Fixed: Environment kinds are changed in the tooling. Changed setup page to reflect this.
**2018-02-22**
* Fixed: ECDF plot was incorrect. As it turns out, the formula was wrong.
* Fixed: Code sample in challenge 2 to get value_count() for yr_renovated was unclear.
* Fixed: Missing instructions for installing Seaborn were added in Challenge 2.
* Fixed: Added instructions to fix a problem with a missing resource provider on Azure.

**2018-02-21**
* Intial version
