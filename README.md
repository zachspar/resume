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
Build and push the Docker image, then deploy using Helm:

```bash
# Build the image
docker build -t your-registry/resume:latest .

# Push to your registry
docker push your-registry/resume:latest

# Deploy with Helm
helm install resume ./helm/resume \
  --set image.repository=your-registry/resume \
  --set image.tag=latest

# Or with ingress enabled
helm install resume ./helm/resume \
  --set image.repository=your-registry/resume \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host=resume.yourdomain.com \
  --set ingress.hosts[0].paths[0].path=/ \
  --set ingress.hosts[0].paths[0].pathType=Prefix
```

### Heroku Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
