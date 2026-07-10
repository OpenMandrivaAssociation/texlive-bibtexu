%global tl_name bibtexu
%global tl_revision 66186

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.72
Release:	%{tl_revision}.1
Summary:	BibTeX variant supporting Unicode (UTF-8), via ICU
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/bibtex-x
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(bibtexu.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An enhanced, portable C version of BibTeX. Unicode is supported via the
ICU library. Originally written by Yannis Haralambous and his students,
and derived from bibtex8, with substantial updates from the Japanese TeX
Development Community, it is now maintained as part of TeX Live.

