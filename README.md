# Python sample app using pipenv package manager

## Running Locally

`pipenv run gunicorn --bind=127.0.0.1:8010 app:app`

## Viewing

`curl http://localhost:8010`

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
