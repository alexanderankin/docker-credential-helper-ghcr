# `docker-credential-helper-ghcr`

see prior art:

* https://github.com/awslabs/amazon-ecr-credential-helper
* https://github.com/mriedmann/acr-docker-credential-helper
* https://github.com/googlecloudplatform/docker-credential-gcr

## installation

### via `apt`

```shell
sudo curl -fsSL https://raw.githubusercontent.com/alexanderankin/docker-credential-helper-ghcr/refs/heads/main/packaging/debian/repository.pub.gpg --output /usr/share/keyrings/docker-credential-helper-ghcr.asc

echo "deb [signed-by=/usr/share/keyrings/docker-credential-helper-ghcr.asc] https://alexanderankin.github.io/docker-credential-helper-ghcr/apt stable main" | sudo tee /etc/apt/sources.list.d/docker-credential-ghcr.list

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-credential-ghcr
```

<details>
<summary>test apt install</summary>

```console
$ docker run --rm -it ubuntu:26.04
# apt-get update >/dev/null 2>&1 && echo ok && apt-get install -y apt-transport-https curl >/dev/null 2>&1 && echo ok
ok
ok
# curl -fsSL https://raw.githubusercontent.com/alexanderankin/docker-credential-helper-ghcr/refs/heads/main/packaging/debian/repository.pub.gpg --output /usr/share/keyrings/docker-credential-helper-ghcr.asc
# echo "deb [signed-by=/usr/share/keyrings/docker-credential-helper-ghcr.asc] https://alexanderankin.github.io/docker-credential-helper-ghcr/apt stable main" > /etc/apt/sources.list.d/docker-credential-ghcr.list && apt-get update >/dev/null 2>&1 && DEBIAN_FRONTEND=noninteractive apt-get install -y docker-credential-ghcr >dev/null 2>&1 && echo ok
ok
# python3 -V
Python 3.14.4
# gh version
gh version 2.46.0 (2025-12-13 Ubuntu 2.46.0-4)
https://github.com/cli/cli/releases/tag/v2.46.0
# docker-credential-helper-ghcr --version
0.0.1
```
</details>

### via homebrew

```shell
brew tap alexanderankin/docker-credential-helper-ghcr https://github.com/alexanderankin/docker-credential-helper-ghcr
brew trust alexanderankin/docker-credential-helper-ghcr
brew install docker-credential-ghcr
```
