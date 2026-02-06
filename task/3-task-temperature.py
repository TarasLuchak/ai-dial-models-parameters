from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    # Lower values (e.g. 0.0–0.3) are more deterministic, higher values are more creative.
    # Try changing this between 0.0 and 1.0 and re-running the script.
    temperature=0.3,
)