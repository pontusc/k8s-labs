## Liveness testing
Deploys 25 images of a python api where the healthcheck has a 10% chance to fail. 
If it fails twice in a row, it will kill that pod and redeploy.
