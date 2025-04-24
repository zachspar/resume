"""
Render HTML resume templates and copy static files to output directory.
"""

import jinja2
import tomllib
import shutil
from pathlib import Path


def mock_url_for(endpoint, **kwargs):
    """
    Mock url_for function for Jinja2 templates.
    Returns static file paths or endpoint routes.
    """
    if endpoint == "static":
        filename = kwargs.get("filename", "")
        return f"/resume/static/{filename}"
    return f"/{endpoint}"


def main():
    # Set up output directory
    output_dir = Path("rendered_artifacts")
    output_dir.mkdir(exist_ok=True)

    # Set up static output directory
    static_output_dir = output_dir / "static"
    static_output_dir.mkdir(exist_ok=True)

    # Copy static files to output directory
    static_dir = Path("static")
    if static_dir.exists():
        shutil.copytree(static_dir, static_output_dir, dirs_exist_ok=True)

    # Set up Jinja2 environment
    template_dir = Path("templates/home")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
    env.globals["url_for"] = mock_url_for  # Add mock url_for to Jinja2 globals

    # Load the template
    template = env.get_template("index_template.html")

    # Load data from TOML file
    with open("resume_config.toml", "rb") as file:
        resume_data = tomllib.load(file)

    # Render the template with the data
    rendered_html = template.render(**resume_data)

    # Save the rendered HTML to a file in output directory
    with open(output_dir / "index.html", "w") as outfile:
        outfile.write(rendered_html)


if __name__ == "__main__":
    main()
