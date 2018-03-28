# Dataflow template for VS-Code

This is a base template to create python dataflow projects with VScode configuration.

The dataflow script just count a how many chatacters has a string no including spaces.

## Computer where was created

The environment where script was created is below:

* MacBook Pro (13-inch, Mid 2012)
  * Processor: 2,5 GHz Intel Core i5
  * Ram: 10 GB 1600 MHz DDR3
  * Disk: 500 GB SATA

## Configuration

This are the steps to configure the environment

### Virtual environment

to Dataflow development I recomended to use VirtualEnv to keep clean python in you machine.

the code below shows how to configure virtualenv for mac.

```bash
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Run in local machine

to run in local machine I create a custom task called run DirectRunner. To run go to taks menu, select **Run task..** and select **run DirectRunner**

## Run in cloud

## Debug

## Install as Template

## git aditional

to untrack changes in task files 

```bash
git update-index --assume-unchanged .vscode/tasks.json
```

to retrack changes in task files 

```bash
git update-index --no-assume-unchanged .vscode/tasks.json
```
