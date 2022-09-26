# Python sample app using pipenv package manager

A basic sample which began life as part of the [Packeto Buildpack](https://github.com/paketo-buildpacks/samples) samples. Designed to illustrate how buildpacks and supply chains work to build and deploy an application. Should work just fine with VMware Tanzu Application Platform and VMware Tanzu Application Service.

## Running Locally

`pipenv run gunicorn --bind=127.0.0.1:8001 app:app`

## Viewing

`curl http://localhost:8001`

## Running on TAP

```bash
tanzu apps workload create python-sample \
  --git-repo https://github.com/benwilcock/python-pipenv \
  --git-branch main \
  --type web \
  --label app.kubernetes.io/part-of=python-sample \
  --annotation autoscaling.knative.dev/minScale=1 \
  --namespace default \
  --tail \
  --yes 
```

## Application Endpoints

1. `/`  HTML home page (shows a single page app containing a static image and some text). Contains a link to the source code.
1. `/messages` REST [GET] (shows a single hardcoded message as part of a list of messages).
1. `/versions` Plaintext (shows the version of Gunicorn used in this app).

## Customisations

For a simple customisation, in the application code (in the `app.py` `hello()` method) change the name of the `client` variable from "VMware" to someone else and then redeploy/restart.

```python
@app.route("/")
def hello():
    client = "VMware"
    return render_template('index.html', client=client)
```

The homepage will then use the new name of the client in the text at the bottom of the page.

## Vulnerability Scanning

Adding a known vulnerability:

Open the Pipfile, and under the `[Packages]` section add the line `ffmpeg = "==1.4"`.

```bash
nano Pipfile
```

Now recreate the `requirements.txt` file (Grype uses this as a list of dependencies):

```bash
pipenv lock --requirements > requirements.txt
```

Now run the Grype scanner on the code folder:

```bash
grype . # Run from this folder
```

Grype should spot the vulnerability and log warnings to the console.

To remove the vulnerability, remove the ffmpeg dependency from the `Pipfile` and recreate the `requirements.txt` again.
