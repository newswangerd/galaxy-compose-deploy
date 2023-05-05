## Steps to deploy Galaxy NG

0. Installer docker compose

1. Clone this repository: `git clone https://github.com/newswangerd/galaxy-compose-deploy.git`

2. Set "HOSTNAME" in `docker-compose.yaml` to the IP address or DNS host that you wish to run galaxy on.

3. Start docker compose: `docker compose up -d`. Give it a minute to spin up and then navigate to https://HOSTNAME in your browser to check if it's running.

4. Create an admin user: `docker compose exec galaxy pulpcore-manager createsuperuser`
