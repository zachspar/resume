# Resume Website
[Check out my website!](https://zachspar.github.io/resume/)

## Create Your Own
If you'd like to use this repo as a template, all you need to do is fork
it and update `resume_config.toml` with your information accordingly.

You should also update any static files to include your headshot if desired.

## Deployment Methods

### GitHub Pages Deployment
By default, this repo will publish to GitHub pages from the `main` or `master` branch.

### Kubernetes Deployment
The CI pipeline automatically builds and pushes the Docker image to GHCR on release.

Deploy using Helm:

```bash
# Deploy with Helm
helm install resume oci://ghcr.io/<username>/resume/chart --version <release-tag>

# Or with ingress enabled
helm install resume oci://ghcr.io/<username>/resume/chart --version <release-tag> \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host=resume.yourdomain.com \
  --set ingress.hosts[0].paths[0].path=/ \
  --set ingress.hosts[0].paths[0].pathType=Prefix
```

### Heroku Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
