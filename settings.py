import os

_CONTAINER_ENV_CONFIGS = {
    "API_PROTOCOL": "https" if os.getenv("PULP_HTTPS", default="true") == "true" else "http",
    "API_HOST": os.getenv("HOSTNAME"),
    "API_PORT": os.getenv("PORT")
}


# Pulp needs an /etc/pulp/settings.py with CONTENT_ORIGIN to start.
CONTENT_ORIGIN='{API_PROTOCOL}://{API_HOST}:{API_PORT}'.format(**_CONTAINER_ENV_CONFIGS)
ALLOWED_EXPORT_PATHS=["/tmp"]
ALLOWED_IMPORT_PATHS=["/tmp"]

GALAXY_API_PATH_PREFIX='/api/galaxy/'
GALAXY_DEPLOYMENT_MODE='standalone'
RH_ENTITLEMENT_REQUIRED='insights'
GALAXY_REQUIRE_CONTENT_APPROVAL=False

ANSIBLE_API_HOSTNAME="{API_PROTOCOL}://{API_HOST}:{API_PORT}".format(**_CONTAINER_ENV_CONFIGS)
ANSIBLE_CONTENT_HOSTNAME="{API_PROTOCOL}://{API_HOST}:{API_PORT}/pulp/content".format(**_CONTAINER_ENV_CONFIGS)

# Pulp container requires this to be set in order to provide docker registry
# compatible token authentication.
# https://docs.pulpproject.org/container/workflows/authentication.html
TOKEN_AUTH_DISABLED=False
TOKEN_SERVER="{API_PROTOCOL}://{API_HOST}:{API_PORT}/token/".format(**_CONTAINER_ENV_CONFIGS)
TOKEN_SIGNATURE_ALGORITHM="ES256"
PUBLIC_KEY_PATH="/src/galaxy_ng/dev/common/container_auth_public_key.pem"
PRIVATE_KEY_PATH="/src/galaxy_ng/dev/common/container_auth_private_key.pem"


# Signing configs
# ENABLE_SIGNING=1

# GALAXY_AUTO_SIGN_COLLECTIONS=True
# GALAXY_REQUIRE_CONTENT_APPROVAL=True
# GALAXY_COLLECTION_SIGNING_SERVICE="ansible-default"
# GALAXY_CONTAINER_SIGNING_SERVICE="container-default"