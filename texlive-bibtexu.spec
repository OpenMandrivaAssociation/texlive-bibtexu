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
Requires(pre):	texlive-tlpkg
Requires:	texlive(bibtexu.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An enhanced, portable C version of BibTeX. Unicode is supported via the
ICU library. Originally written by Yannis Haralambous and his students,
and derived from bibtex8, with substantial updates from the Japanese TeX
Development Community, it is now maintained as part of TeX Live.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu/examples
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu/examples/test.bbl
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu/examples/test.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu/examples/test.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtexu/examples/test.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibtexu.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibtexu.man1.pdf
