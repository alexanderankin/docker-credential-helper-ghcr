class DockerCredentialGhcr < Formula
  desc "Docker credential helper for GHCR backed by GitHub CLI"
  homepage "https://github.com/alexanderankin/docker-credential-helper-ghcr"

  version "0.0.2"
  sha256 "b02a152d08439429e2eebbec5a7011cd3f353933fd91a8f073846b3b78a80dd9"
  url "https://github.com/alexanderankin/docker-credential-helper-ghcr/releases/download/v#{version}/docker-credential-ghcr.py"

  license "Apache-2.0"

  depends_on "gh"
  depends_on "python@3.14"

  def install
    bin.install "docker-credential-ghcr.py" => "docker-credential-helper-ghcr"
    # bin.install_symlink "docker-credential-helper-ghcr" => "docker-credential-ghcr"
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/docker-credential-helper-ghcr --version")
  end
end
