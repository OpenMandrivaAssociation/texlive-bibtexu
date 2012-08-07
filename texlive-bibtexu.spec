# revision 26693
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-bibtexu
Version:	20120807
Release:	1
Summary:	TeXLive bibtexu package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtexu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-bibtexu.bin

%description
TeXLive bibtexu package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/bibtexu/00readme.txt
%doc %{_texmfdir}/doc/bibtexu/HISTORY
%doc %{_texmfdir}/doc/bibtexu/csfile.txt
%doc %{_texmfdir}/doc/bibtexu/file_id.diz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
