# DevOps Tests
## Author Mahtarr Jeng

Hi everyone, welcome and this is my solutions for the devops test

## Automation Test

This vagrant project installs and bootstraps an apache server which is running a static html file:

* Vagrant has a built in support for automated provisionning, therefore, a shell script is wriiten to setup an Apache webserver

* Then a html content is added which will be served by the webserver

* Port forwarding is added to access apache in our guest machine

     Vagrant's networking features gives additional options for accessing the machine from our host machine. Port Forwarding is 
     the option used and this allows access to a port on your own machine, but actually have all the network traffic forwarded to a specific port on the guest machine.

* A Vagrantfile is provided to allow you to test the code:

     by simply running `vagrant up`

     Once the machine is booted up load 'http://127.0.0.1:4567' in your browser, You should see a web page that is being served from the virtual machine that was automatically setup by Vagrant.


## Coding Test

This project builds a restful Api in Python that is used to store user details, using the flask framework:

* The required library and dependencies were installed using `pip install flask-restful`

* Pipenv is used to create two new files, Pipfile and Pipfile.lock, in the project directory,    and a new virtual environment, `pip install pipenv --three` flag initialise the project to use  Python 3, Otherwise the default version of Python will be used

* To run this project:
      open a terminal
      cd to the folder containing app.py 
      then run `python app.py`
      load http://127.0.0.1:5000//user/<string:name> in browser

      Note <string:name> = ["Amy","Ida","Adam"]


## Infrastructure Test

* In this project I have provisioned an AWS ec2 instance using terraform;

* My approach is to separate the terraform files and variabise my inputs this is very helpful     for debugging:

     *    A modules is used to create lightweight abstractions to describe the infrastructure in terms of its architecture,          rather than directly in terms of physical objects.

     *    The .tf files in the working directory when terraform plan or terraform apply is run will form the root module.

     *    tree ec2_instance

               ├── ami.tf
               ├── instance.tf
               ├── outputs.tf
               ├── provider.tf
               ├── variables.tf
