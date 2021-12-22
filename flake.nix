{
  inputs = {
    nixpkgs.url = github:nixos/nixpkgs/nixos-21.11;
    flake-utils.url = github:numtide/flake-utils;
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        packages.hello = pkgs.hello;

        devShell = pkgs.mkShell {
          buildInputs = with pkgs; with python3Packages; [
            python3Full
            pyright
            autopep8
          ];
        };
      });
}

