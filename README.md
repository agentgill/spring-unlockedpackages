# Salesforce Weekly - Getting started with Unlocked Packages

## Installation Instructions

1. Setup your environment

- Sign up for a Spring '19 pre-release org and enable Dev Hub
- Install the pre-release version of the Salesforce CLI
- Install Visual Studio Code
- Install the Visual Studio Code Salesforce extensions

2. Clone this repository

```
git clone git@github.com:agentgill/spring19-unlockedpackages.git
```

3. CD into new directory

4. Set sfdx defaultuser to be your source / production org

```
sfdx force:config:set defaultusername=xxx
```

5. Edit sfdx-project.json and set the path for your first package (e.g application-package) -

```
{
  "packageDirectories": [
    {
      "path": "application-package",
      "default": true
    }
  ],
  "namespace": "",
  "sfdcLoginUrl": "https://login.salesforce.com",
  "sourceApiVersion": "45.0"
}
```

6. mkdir which matches path from step 5 (e.g. application-package)

## Create your package metadata source

7. Pull packaging source metadata locally

Easy way to build your package.xml using a simple python script

- Add list of items to scripts/Build.csv
- Run following bash script

```
. pull.sh
```

- this will out to manifest/package.xml

Alternative ways to generate your package.xml file

- Use an IDE like **Illuiminated Cloud**
- Use an online app like [Package Builder](https://packagebuilder.herokuapp.com/)

If you are metadata magician, you can grab lots metadata like this:

```
sfdx force:source:retrieve -m CustomObject,Layout
```

This will pull down custom objects and all layouts - you can then manual narrow your package source down to what is required for your package

## Create your first package

Let's create our package using the source from the path specificed in the sfdx-project.json

-v our packaging org  
-r the path to the source (e.g. application-packaging)  
-n the name of the package (will also become the package alias)  
-e no namespace  
-d description of the package  
-t type of package e.g. unlocked  

```
sfdx force:package:create -v play -r application-package -n application-package -e -d "application package" -t unlocked
```

Review the sfdx-project.json for details of package

## Create your first package version

Let's create an installable version of our package

-p this is our package name/alias  
-d the path to the source  
-x no installation key (no password in other words)  
-w wait for X (syncronously wait for the package version is created)  
-v our packaging org  

```
sfdx force:package:version:create -p application-package -d application-package -x --wait 10 -v play
```

Review the sfdx-project.json for details of package version

## Useful Packaging Commands

List Packages

```
sfdx force:package:list -v play
```

View Versions

```
sfdx force:package:version:list -v play
```