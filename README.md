[![Dev Environment Prebuilds](https://github.com/eTcilopp/temp-functions-from-zero/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/eTcilopp/temp-functions-from-zero/actions/workflows/codespaces/create_codespaces_prebuilds)

# temp-functions-from-zero
A repo to learn functions


## Step 1:Configure Development Environment

* Configure GitHub Cidescpaces orthe equivalent
* Create scaffold fo structure of project" `Makefile` `requirements.txt
* Optional (setup vitrualenv) (install python outside of requirements.txt)

## Step 2: Get interactive debugging working

* use IPython and ipdb
```
x = 1
y = 2
import ipdb; ipdb.set_trace()
print(x + y)
```