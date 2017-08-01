{ nixpkgs ? (import <nixpkgs> {})
}:

with nixpkgs.pkgs;
with python36Packages;

stdenv.mkDerivation {
  name = "qa_gen-env";
  buildInputs = [
     python36Full
     python36Packages.virtualenv
     python36Packages.pip

     faker
     dateutil
     matplotlib
     numpy
     sympy];
  src = null;
  shellHook = ''
    SOURCE_DATE_EPOCH=$(date +%s)
    virtualenv --no-setuptools venv
    export PATH=$PWD/venv/bin:$PATH
  '';
}
