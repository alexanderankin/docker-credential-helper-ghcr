class DockerCredentialGhcr < Formula
  desc "Docker credential helper for GHCR backed by GitHub CLI"
  homepage "https://github.com/alexanderankin/docker-credential-helper-ghcr"

  version "0.0.2"
  sha256 "b0f9faceeef625407b8e0ee454072e8c88694b95b4b683ffa62adf67417054db"
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
