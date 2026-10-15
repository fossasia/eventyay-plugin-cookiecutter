import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml
from cookiecutter.main import cookiecutter


class WorkflowPathsTest(unittest.TestCase):
    def test_generated_checkout_can_be_renamed(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            generated = Path(
                cookiecutter(str(Path.cwd()), no_input=True, output_dir=str(parent))
            )
            checkout = parent / "checkout with a different name"
            generated.rename(checkout)
            workflow = yaml.safe_load(
                (checkout / ".github/workflows/tests.yml").read_text()
            )
            install = next(
                step
                for step in workflow["jobs"]["test"]["steps"]
                if step.get("name") == "Install Eventyay and the plugin"
            )
            core = parent / "eventyay/app"
            core.mkdir(parents=True)
            tools = parent / "bin"
            tools.mkdir()
            uv = tools / "uv"
            uv.write_text(
                "#!/usr/bin/env python3\nimport json,os,sys\n"
                "if sys.argv[1:3] == ['pip','install']:\n"
                " path=sys.argv[sys.argv.index('-e')+1]\n"
                " assert os.path.isfile(os.path.join(path,'pyproject.toml')), path\n"
                " open(os.environ['INSTALL_RECORD'],'w').write(json.dumps(path))\n"
            )
            uv.chmod(0o755)
            record = parent / "installed.json"
            env = {
                **os.environ,
                "PATH": str(tools) + os.pathsep + os.environ["PATH"],
                "GITHUB_WORKSPACE": str(checkout),
                "INSTALL_RECORD": str(record),
            }
            subprocess.run(
                install["run"],
                shell=True,
                cwd=checkout / install["working-directory"],
                env=env,
                check=True,
            )
            self.assertEqual(Path(json.loads(record.read_text())), checkout)

    def test_template_discovery_uses_the_cloned_environment(self):
        workflow = yaml.safe_load(Path(".github/workflows/run.yml").read_text())
        step = next(
            step
            for step in workflow["jobs"]["test"]["steps"]
            if step.get("name") == "Verify plugin discovery"
        )
        with tempfile.TemporaryDirectory() as directory:
            checkout = Path(directory) / "template"
            generated = checkout / "eventyay-superplugin"
            generated.mkdir(parents=True)
            python = checkout.parent / "eventyay/app/.venv/bin/python"
            python.parent.mkdir(parents=True)
            python.write_text("#!/bin/sh\nprintf 'correct-environment\\n'\n")
            python.chmod(0o755)
            result = subprocess.run(
                step["run"],
                shell=True,
                cwd=checkout / step["working-directory"],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.stdout.strip(), "correct-environment")
