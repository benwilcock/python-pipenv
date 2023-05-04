# Python

This app contains source code for a Python application that can be built and deployed automatically by the Tanzu Application Platform. The app includes a web page created using ([Flask](https://flask.palletsprojects.com/en/2.3.x/)) and a basic REST API. This application was initially created using an Accelerator for Python applications.

Features at a glance:

* A Python using the Pipenv packaging method
* Flask to provide web page templating and a landing page for the site
* A REST API that allows you to GET `/messages` (returns a JSON string built in `app.py`)
* Backstage TechDocs using Markdown (see `mkdocs.yml` and `docs/index.md`)

Navigating your broswer to **http(s)://&lt;your.hosting.url&gt;:&lt;port&gt;** should show the following screen:

![supply chain diagram](https://github.com/benwilcock/python-pipenv/raw/main/static/tap-into-prod.png "Composable and Modular - TAP Supply Chains")

## Running on the VMware Tanzu Application Platform

[Watch it deploy on Tanzu Application Platform.](https://via.vmw.com/tap-python-sc)

The application can be deployed via the `tanzu` cli using a command line similar to the one shown below. You may need to modify this command depending needs of the supply chain you're using.

```bash
tanzu apps workload create python-pipenv \
  --git-repo https://github.com/benwilcock/python-pipenv \
  --git-branch main \
  --type web \
  --label app.kubernetes.io/part-of=python-pipenv \
  --label apps.tanzu.vmware.com/has-tests=true \
  --param-yaml testing_pipeline_matching_labels='{"apps.tanzu.vmware.com/pipeline":"test", "apps.tanzu.vmware.com/language":"python"}' \
  --annotation autoscaling.knative.dev/minScale=1 \
  --tail \
  --yes
```

## Customisations

For a simple customisation, in the application code (in the `app.py` `hello()` method) change the name of the `client` variable from "VMware" to something else and then redeploy/restart.

```python
@app.route("/")
def hello():
    client = "VMware"
    return render_template('index.html', client=client)
```