Name:		texlive-bibtexu
Version:	20111101
Release:	1
Summary:	TeXLive bibtexu package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-bibtexu.bin
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive bibtexu package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
