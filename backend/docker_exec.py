import docker

client = docker.from_env()

def run_code_in_sandbox(code, lang="python"):
    container = client.containers.run(
        "python:3.10",
        f"python -c '{code}'",
        detach=False,
        remove=True
    )
    return container
