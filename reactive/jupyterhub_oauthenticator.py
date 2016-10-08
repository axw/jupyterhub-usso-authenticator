import subprocess

from charms.reactive import when, when_not, set_state
from charmhelpers.core import templating

@when_not('jupyterhub-oauthenticator.installed')
def install_jupyterhub_oauthenticator():
    subprocess.check_call(
        ['python3', 'setup.py', 'install'],
        cwd='oauthenticator',
    )
    set_state('jupyterhub-oauthenticator.installed')


@when('jupyterhub-oauthenticator.installed')
@when('jupyterhub.available')
def update_config(jupyterhub):
    # TODO(axw) make the class and service configurable
    jupyterhub.set_authenticator('oauthenticator.ubuntu.UbuntuSSOAuthenticator', {})

